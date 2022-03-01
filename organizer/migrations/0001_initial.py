# Generated by Django 3.2.9 on 2021-11-10 16:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Tag",
            fields=[
                (
                    "id",
                    models.AutoField(
                        primary_key=True, serialize=False
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=50, unique=True
                    ),
                ),
                (
                    "slug",
                    models.SlugField(
                        help_text="A lable for URL config.",
                        unique=True,
                    ),
                ),
            ],
            options={
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="Startup",
            fields=[
                (
                    "id",
                    models.AutoField(
                        primary_key=True, serialize=False
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        db_index=True, max_length=50
                    ),
                ),
                (
                    "slug",
                    models.SlugField(
                        help_text="A label for URL config.",
                        unique=True,
                    ),
                ),
                ("description", models.TextField()),
                (
                    "founded_date",
                    models.DateField(
                        verbose_name="date founded"
                    ),
                ),
                (
                    "contact",
                    models.EmailField(max_length=254),
                ),
                (
                    "website",
                    models.URLField(max_length=250),
                ),
                (
                    "tags",
                    models.ManyToManyField(
                        to="organizer.Tag"
                    ),
                ),
            ],
            options={
                "ordering": ["name"],
                "get_latest_by": "founded_date",
            },
        ),
        migrations.CreateModel(
            name="NewsLink",
            fields=[
                (
                    "id",
                    models.AutoField(
                        primary_key=True, serialize=False
                    ),
                ),
                ("title", models.CharField(max_length=50)),
                ("slug", models.SlugField()),
                (
                    "pub_date",
                    models.DateField(
                        verbose_name="date published"
                    ),
                ),
                ("link", models.URLField(max_length=250)),
                (
                    "startup",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="organizer.startup",
                    ),
                ),
            ],
            options={
                "verbose_name": "news article",
                "ordering": ["-pub_date"],
                "get_latest_by": "pub_date",
                "unique_together": {("slug", "startup")},
            },
        ),
    ]
