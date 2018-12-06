import graphene

import item_builder.schema
import guides.schema


class Query(item_builder.schema.Query, guides.schema.Query, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)
