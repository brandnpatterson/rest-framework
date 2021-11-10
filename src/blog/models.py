from datetime import date
from django.db.models import (
    CharField,
    DateField,
    ManyToManyField,
    Model,
    SlugField,
    TextField,
)
from organizer.models import Startup, Tag


class Post(Model):
    title = CharField(max_length=100)
    slug = SlugField(
        max_length=100,
        help_text="A label for URL config.",
        unique_for_month="pub_date",
    )
    text = TextField()
    pub_date = DateField(
        "date published", default=date.today
    )
    startup = ManyToManyField(
        Startup, related_name="blog_posts"
    )
    tags = ManyToManyField(Tag, related_name="blog_posts")

    class Meta:
        get_latest_by = "pub_date"
        ordering = ["-pub_date", "title"]
        verbose_name = "blog post"

    def __str__(self):
        date_str = self.pub_date.strftime("%Y-%m-%d")
        return f"{self.title} on {date_str}"
