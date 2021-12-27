from rest_framework.fields import (
    CharField,
    DateField,
    EmailField,
    IntegerField,
    SlugField,
    URLField,
)
from rest_framework.serializers import (
    HyperlinkedIdentityField,
    HyperlinkedModelSerializer,
    ModelSerializer,
)

from .models import NewsLink, Startup, Tag


class TagSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"
        extra_kwargs = {
            "url": {
                "lookup_field": "slug",
                "view_name": "api-tag-detail",
            }
        }


class StartupSerializer(HyperlinkedModelSerializer):
    tags = TagSerializer(many=True)

    class Meta:
        model = Startup
        fields = "__all__"
        extra_kwargs = {
            "url": {
                "lookup_field": "slug",
                "view_name": "api-startup-detail",
            }
        }


class NewsLinkSerializer(ModelSerializer):
    class Meta:
        model = NewsLink
        fields = "__all__"
