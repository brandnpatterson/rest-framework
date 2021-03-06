# Generated by Django 3.2.9 on 2022-02-28 21:40

from django.db import migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_alter_post_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="slug",
            field=django_extensions.db.fields.AutoSlugField(
                blank=True,
                editable=False,
                help_text="A label for URL config.",
                populate_from=["title"],
            ),
        ),
    ]
