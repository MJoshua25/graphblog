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
            'titre': ['exact', 'icontains', 'istartswith'],
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
            'first_name': ['exact', 'icontains', 'istartswith'],
            'last_name': ['exact', 'icontains', 'istartswith'],
            'username': ['exact', 'icontains', 'istartswith'],
        }
        interfaces = (relay.Node,)
        connection_class = ExtendConnection


class TagNode(DjangoObjectType):
    class Meta:
        model = models.Tag
        # Allow for some more advanced filtering here
        fields = "__all__"
        filter_fields = {
            'titre': ['exact', 'icontains', 'istartswith'],
            'titre_slug': ['exact', 'icontains', 'istartswith'],
            'status': ['exact'],
        }
        interfaces = (relay.Node,)
        connection_class = ExtendConnection


class ArticleNode(DjangoObjectType):
    class Meta:
        model = models.Article
        # Allow for some more advanced filtering here
        fields = "__all__"
        filter_fields = {
            'tags': ['exact'],
            'titre': ['exact', 'icontains', 'istartswith'],
            'titre_slug': ['exact', 'icontains', 'istartswith'],
            'status': ['exact'],
            'categorie': ['exact'],
        }
        interfaces = (relay.Node,)
        connection_class = ExtendConnection


class CommentaireNode(DjangoObjectType):
    class Meta:
        model = models.Commentaire
        # Allow for some more advanced filtering here
        fields = "__all__"
        filter_fields = {
            'user': ['exact'],
            'user__username': ['exact', 'icontains', 'istartswith'],
            'article': ['exact'],
            'status': ['exact'],
        }
        interfaces = (relay.Node,)
        connection_class = ExtendConnection


class Query(graphene.ObjectType):
    Categorie = relay.Node.Field(CategorieNode)
    all_Categories = DjangoFilterConnectionField(CategorieNode)

    User = relay.Node.Field(UserNode)
    all_users = DjangoFilterConnectionField(UserNode)

    Tag = relay.Node.Field(TagNode)
    all_tags = DjangoFilterConnectionField(TagNode)

    Article = relay.Node.Field(ArticleNode)
    all_articles = DjangoFilterConnectionField(ArticleNode)

    Commentaire = relay.Node.Field(CommentaireNode)
    all_commentaires = DjangoFilterConnectionField(CommentaireNode)