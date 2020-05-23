from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphene import Connection
from django_filters import FilterSet, OrderingFilter
import graphene
from graphql_jwt.decorators import login_required

from . import models
from django.contrib.auth.models import User



class ExtendConnection(Connection):
    class Meta:
        abstract = True

    total_count = graphene.Int()
    edge_count = graphene.Int()

    def resolve_total_count(root, info, **kwargs):
        return root.length

    def resolve_edge_count(root, info, **kwargs):
        return len(root.edges)


class CategorieNode(DjangoObjectType):
    class Meta:
        model = models.Categorie
        # Allow for some more advanced filtering here
        fields = "__all__"
        filter_fields = {
            'nom': ['exact', 'icontains', 'istartswith'],
            'titre_slug': ['exact', 'icontains', 'istartswith'],
            'status': ['exact'],
        }
        interfaces = (relay.Node,)
        connection_class = ExtendConnection


class UserNode(DjangoObjectType):
    class Meta:
        model = models.User
        # Allow for some more advanced filtering here
        fields = "__all__"
        filter_fields = {
            'first_name': ['exact'],
            'bio': ['exact', 'icontains', 'istartswith'],
            'status': ['exact'],
        }
        interfaces = (relay.Node,)
        connection_class = ExtendConnection


class TagueNode(DjangoObjectType):
    class Meta:
        model = models.Tague
        # Allow for some more advanced filtering here
        fields = "__all__"
        filter_fields = {
            'nom': ['exact', 'icontains', 'istartswith'],
            'status': ['exact'],
        }
        interfaces = (relay.Node,)
        connection_class = ExtendConnection
