from django.shortcuts import (
    get_object_or_404,
    redirect,
    render,
)
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .forms import TagForm
from .models import NewsLink, Startup, Tag
from .serializers import NewsLinkSerializer


class TagList(ListView):
    queryset = Tag.objects.all()
    template_name = "tag/list.html"


class TagDetail(DetailView):
    queryset = Tag.objects.all()
    template_name = "tag/detail.html"


class TagCreate(CreateView):
    form_class = TagForm
    model = Tag
    template_name = "tag/form.html"
    extra_context = {"update": False}


class TagUpdate(CreateView):
    form_class = TagForm
    model = Tag
    template_name = "tag/form.html"
    extra_context = {"update": True}


class TagDelete(DeleteView):
    form_class = TagForm
    model = Tag
    template_name = "tag/confirm_delete.html"
    success_url = reverse_lazy("tag_list")


class StartupList(ListView):
    queryset = Startup.objects.all()
    template_name = "startup/list.html"


class StartupDetail(DetailView):
    queryset = Startup.objects.all()
    template_name = "startup/detail.html"
