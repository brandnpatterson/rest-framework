from django.shortcuts import get_object_or_404
from django.views.generic import ListView, View
from .models import Post


class PostList(ListView):
    model = Post
    template_name = "post/list.html"


class PostDetail(View):
    def get(self, request, year, month, slug):
        post = get_object_or_404(
            Post,
            post_date__year=year,
            post_date__month=month,
            slug=slug,
        )
        context = {"post", post}

        return render(request, "post/detail.html", context)
