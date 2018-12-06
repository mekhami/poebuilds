from django.contrib.postgres.search import SearchVector, SearchRank, SearchQuery
import graphene
from graphene_django.types import DjangoObjectType
from taggit.models import Tag

from guides.models import Guide, CharacterChoices



class Guide(DjangoObjectType):
    class Meta:
        model = Guide
        exclude_fields = ('tags',)

    tags = graphene.List(graphene.String)

    def resolve_tags(self, info):
        return self.tags


class SearchInput(graphene.InputObjectType):
    term = graphene.String()
    character_class = graphene.Enum.from_enum(CharacterChoices)
    ascendancy = graphene.String()
    primary_skill = graphene.String()


class Query(object):
    guides = graphene.List(Guide, term=graphene.String(), search=graphene.Argument(SearchInput))
    tags_list = graphene.List(graphene.String, name=graphene.String())

    def resolve_guides(self, info, term=None, search):
        if term:
            vector = SearchVector('name', 'primary_skill', 'content', 'items')
            query = SearchQuery(term)
            return Guide.objects.annotate(rank=SearchRank(vector, query)).order_by('-rank')
        else:
            return None

    def resolve_tags_list(self, info, name=None):
        if name:
            return Tag.objects.filter(name__icontains=name)[0:50]
        else:
            return Tag.objects.all()[0:50]
