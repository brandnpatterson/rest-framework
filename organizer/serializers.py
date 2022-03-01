from rest_framework.reverse import reverse
from rest_framework.serializers import (
    HyperlinkedModelSerializer,
    HyperlinkedRelatedField,
    ModelSerializer,
    SerializerMethodField,
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

    def create(self, validated_data):
        tag_data_list = validated_data.pop("tags")
        startup = Startup.objects.create(**validated_data)
        tag_list = Tag.objects.bulk_create(
            [Tag(**tag_data) for tag_data in tag_data_list]
        )
        startup.tags.add(*tag_list)
        return startup


class NewsLinkSerializer(ModelSerializer):
    url = SerializerMethodField()
    startup = HyperlinkedRelatedField(
        queryset=Startup.objects.all(),
        lookup_field="slug",
        view_name="api-startup-detail",
    )

    class Meta:
        model = NewsLink
        exclude = ("id",)

    def get_url(self, newslink):
        return reverse(
            "api-newslink-detail",
            kwargs={
                "startup_slug": newslink.startup.slug,
                "newslink_slug": newslink.slug,
            },
            request=self.context["request"],
        )
