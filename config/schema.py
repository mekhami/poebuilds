import graphene

import item_builder.schema


class Query(item_builder.schema.Query, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)
