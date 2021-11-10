from django.db.models import (
    CharField,
    DateField,
    ManyToManyField,
    Model,
    SlugField,
    TextField,
)


class Tag(Model):
    name = CharField(max_length=50, unique=True)
    slug = SlugField(
        max_length=50,
        unique=True,
        help_text="A lable for URL config.",
    )

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Startup(Model):
    name = CharField(max_length=50, db_index=True)
    slug = SlugField(
        max_length=50,
        unique=True,
        help_text="A label for URL config.",
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
    title = CharField(max_length=50)
    slug = SlugField(max_length=50)
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
