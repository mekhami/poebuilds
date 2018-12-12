from django.contrib.postgres.search import SearchVector, SearchRank, SearchQuery
import graphene
from graphene_django.types import DjangoObjectType
from graphene_django.forms.mutation import DjangoModelFormMutation
from taggit.models import Tag

from guides import models
from guides.forms import GuideForm



class Guide(DjangoObjectType):
    class Meta:
        model = models.Guide
        exclude_fields = ('tags',)

    tags = graphene.List(graphene.String)

    def resolve_tags(self, info):
        return self.tags


class SearchInput(graphene.InputObjectType):
    term = graphene.String()
    character_class = graphene.Enum.from_enum(models.CharacterChoices)
    ascendancy = graphene.String()
    primary_skill = graphene.String()


class GuideInput(graphene.InputObjectType):
    title = graphene.String()
    character_class = graphene.String()
    content = graphene.types.json.JSONString()
    items = graphene.types.json.JSONString()


class GuidePayload(graphene.ObjectType):
    guide = graphene.Field(lambda: Guide)
    errors = graphene.types.json.JSONString()


class GuideMutation(graphene.Mutation):
    class Arguments:
        guide_input = graphene.Argument(lambda: GuideInput)

    guide_payload = graphene.Field(lambda: GuidePayload)

    @staticmethod
    def mutate(self, info, guide_input):
        form = GuideForm(guide_input)
        if form.is_valid():
            guide = form.save()
            return GuidePayload(guide=guide, errors=None)
        else:
            return GuidePayload(errors=form.errors, guide=None)


class Query(object):
    guides = graphene.List(Guide, term=graphene.String(), search=graphene.Argument(SearchInput))
    tags_list = graphene.List(graphene.String, name=graphene.String())

    def resolve_guides(self, info, search, term=None):
        if term:
            vector = SearchVector('name', 'primary_skill', 'content', 'items')
            query = SearchQuery(term)
            return models.Guide.objects.annotate(rank=SearchRank(vector, query)).order_by('-rank')
        elif search:
            return None
        else:
            return models.Guide.objects.order_by('-updated_at')[:20]

    def resolve_tags_list(self, info, name=None):
        if name:
            return Tag.objects.filter(name__icontains=name)[0:50]
        else:
            return Tag.objects.all()[0:50]


class Mutation(object):
    guide_mutation = GuideMutation.Field()
