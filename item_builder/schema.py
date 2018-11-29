import json

import graphene


class BaseItem(graphene.ObjectType):
    icon = graphene.String()
    name = graphene.String()
    frame_type = graphene.Int()


class Query(object):
    base_item = graphene.Field(BaseItem, name=graphene.String())

    def resolve_base_item(self, info, name, **kwargs):
        with open('item_builder/item_data/itemdata.json', 'r') as file:
            items = json.load(file)
        found = next((d for (index, d) in enumerate(items) if d['name'] == name), None)
        if found:
            return BaseItem(
                    icon=found['icon'], 
                    name=found['name'],
                    frame_type=found['frame'])
