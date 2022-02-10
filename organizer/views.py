from django.views.generic import DetailView, ListView
from .models import Startup, Tag


class TagList(ListView):
    queryset = Tag.objects.all()
    template_name = "tag/list.html"


class TagDetail(DetailView):
    queryset = Tag.objects.all()
    template_name = "tag/detail.html"


class StartupList(ListView):
    queryset = Startup.objects.all()
    template_name = "startup/list.html"


class StartupDetail(DetailView):
    queryset = Startup.objects.all()
    template_name = "startup/detail.html"
