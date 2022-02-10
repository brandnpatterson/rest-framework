from django.shortcuts import get_object_or_404
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
)
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import (
    NewsLinkSerializer,
    StartupSerializer,
    TagSerializer,
)
from .models import NewsLink, Startup, Tag


class TagAPIDetail(RetrieveAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    lookup_field = "slug"


class TagAPIList(ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class StartupAPIDetail(RetrieveAPIView):
    queryset = Startup.objects.all()
    serializer_class = StartupSerializer
    lookup_field = "slug"


class StartupAPIList(ListAPIView):
    queryset = Startup.objects.all()
    serializer_class = StartupSerializer


class NewsLinkAPIDetail(RetrieveAPIView):
    queryset = NewsLink.objects.all()
    serializer_class = NewsLinkSerializer

    def get_object(self):
        startup_slug = self.kwargs.get("startup_slug")
        newslink_slug = self.kwargs.get("startup_slug")

        queryset = self.filter_queryset(self.get_queryset())

        newslink = get_object_or_404(
            queryset,
            slug=newslink_slug,
            startup_slug=startup_slug,
        )
        self.check_object_permissions(
            self.request, newslink
        )

        return newslink


class NewsLinkAPIList(ListAPIView):
    queryset = NewsLink.objects.all()
    serializer_class = NewsLinkSerializer
