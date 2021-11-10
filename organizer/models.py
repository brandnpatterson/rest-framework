from django.db.models import (
    CASCADE,
    AutoField,
    CharField,
    DateField,
    EmailField,
    ForeignKey,
    ManyToManyField,
    Model,
    TextField,
    URLField
)
from django_extensions.db.fields import AutoSlugField


class Tag(Model):
    id = AutoField(primary_key=True)
    name = CharField(max_length=50, unique=True)
    slug = AutoSlugField(
        max_length=50,
        help_text="A label for URL config.",
        populate_from=["name"],
    )

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Startup(Model):
    id = AutoField(primary_key=True)
    name = CharField(max_length=50, db_index=True)
    slug = AutoSlugField(
        max_length=50,
        help_text="A label for URL config.",
        populate_from=["name"],
    )
    description = TextField()
    founded_date = DateField("date founded")
    contact = EmailField()
    website = URLField(max_length=250)
    tags = ManyToManyField(Tag)

    class Meta:
        get_latest_by = "founded_date"
        ordering = ["name"]

    def __str__(self):
        return self.name


class NewsLink(Model):
    id = AutoField(primary_key=True)
    title = CharField(max_length=50)
    slug = AutoSlugField(
        max_length=50,
        help_text="A label for URL config.",
        populate_from=["title"],
    )
    pub_date = DateField("date published")
    link = URLField(max_length=250)
    startup = ForeignKey(Startup, on_delete=CASCADE)

    class Meta:
        get_latest_by = "pub_date"
        ordering = ["-pub_date"]
        unique_together = (("slug", "startup"),)
        verbose_name = "news article"

    def __str__(self):
        return f"{self.startup}: {self.title}"
