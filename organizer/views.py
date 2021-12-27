from django.shortcuts import (
    get_list_or_404,
    get_object_or_404,
)
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import StartupSerializer, TagSerializer
from .models import Startup, Tag


class TagAPIList(APIView):
    def get(self, request):
        tag_list = get_list_or_404(Tag)
        serialized = TagSerializer(
            tag_list,
            many=True,
            context={"request": request},
        )

        return Response(serialized.data)


class TagAPIDetail(APIView):
    def get(self, request, slug):
        tag = get_object_or_404(Tag, slug=slug)
        serialized = TagSerializer(
            tag, context={"request": request}
        )

        return Response(serialized.data)


class StartupAPIList(APIView):
    def get(self, request):
        startup = get_list_or_404(Startup)
        serialized = StartupSerializer(
            startup,
            many=True,
            context={"request": request},
        )

        return Response(serialized.data)


class StartupAPIDetail(APIView):
    def get(self, request, slug):
        startup = get_object_or_404(Startup, slug=slug)
        serialized = StartupSerializer(
            startup, context={"request": request}
        )

        return Response(serialized.data)
