from datetime import date

from django.db.models import (
    AutoField,
    CharField,
    DateField,
    ManyToManyField,
    Model,
    TextField,
)
from django_extensions.db.fields import AutoSlugField

from organizer.models import Startup, Tag


class Post(Model):
    id = AutoField(primary_key=True)
    title = CharField(max_length=100)
    slug = AutoSlugField(
        max_length=50,
        help_text="A label for URL config.",
        populate_from=["name"],
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
