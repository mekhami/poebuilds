import json
import requests
import urllib

from graphql import GraphQLError
import graphene

from .mappings import BaseItem as BaseItemMapping
from .mappings import ItemMod as ItemModMapping

CARGO_FSTRING = 'https://pathofexile.gamepedia.com/api.php?action=cargoquery&tables={tables}&fields={fields}&where={where}&format=json'


class SizeField(graphene.ObjectType):
    width = graphene.Int()
    height = graphene.Int()


class DescriptionsField(graphene.ObjectType):
    flavour_text = graphene.String()
    description = graphene.String()


class BaseItem(graphene.ObjectType):
    id = graphene.Int()
    icon = graphene.String()
    name = graphene.String()
    frame = graphene.Int()
    type = graphene.String()
    category = graphene.String()
    group = graphene.String()
    mods = graphene.List(lambda: ItemMod)
    size = graphene.Field(lambda: SizeField)
    descriptions = graphene.Field(lambda: DescriptionsField)

    def resolve_descriptions(self, info):
        formatted = CARGO_FSTRING.format(
                tables='items',
                fields='description,flavour_text',
                where='name="{}"'.format(self.name))
        response = requests.get(formatted)
        response = response.json()['cargoquery'][0]['title']
        return DescriptionsField(description=response['description'], flavour_text=response['flavour text'])

    def resolve_size(self, info):
        formatted = CARGO_FSTRING.format(
                tables='items',
                fields='size_x,size_y', 
                where='name="{}"'.format(self.name))
        response = requests.get(formatted)
        response = response.json()['cargoquery'][0]['title']
        return SizeField(width=response['size x'], height=response['size y'])

    def resolve_mods(self, info):
        with open('item_builder/item_data/uniques.json', 'r') as file:
            uniques = json.load(file)
        found = next((d for (index, d) in enumerate(uniques['uniques']) if d['name'] == self.name), None)
        if not found:
            return []
        return [ItemModMapping(**mod) for mod in found['mods']]


class ItemMod(graphene.ObjectType):
    name_orig = graphene.String()
    ranges = graphene.List(graphene.List(graphene.Int))
    name = graphene.String()
    values = graphene.List(graphene.Int)
    is_variable = graphene.Boolean()


class Query(object):
    base_item = graphene.Field(BaseItem, name=graphene.String())
    base_item_list = graphene.List(BaseItem, name=graphene.String())

    def resolve_base_item_list(self, info, name, **kwargs):
        with open('item_builder/item_data/itemdata.json', 'r') as file:
            items = json.load(file)
        foundList = list({d['name']:d for d in items if d['name'].lower().startswith(name.lower())}.values())
        if not foundList:
            return []
        return [BaseItemMapping(**found) for found in foundList]

    def resolve_base_item(self, info, name, **kwargs):
        with open('item_builder/item_data/itemdata.json', 'r') as file:
            items = json.load(file)
        found = next((d for (index, d) in enumerate(items) if d['name'] == name), None)
        if not found:
            raise GraphQLError('An item by that name was not found.')
        return BaseItemMapping(**found)
