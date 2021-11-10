# Generated by Django 3.2.9 on 2021-11-10 16:49

import django_extensions.db.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organizer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newslink',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(blank=True, editable=False, help_text='A label for URL config.', populate_from=['title']),
        ),
        migrations.AlterField(
            model_name='startup',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(blank=True, editable=False, help_text='A label for URL config.', populate_from=['name']),
        ),
        migrations.AlterField(
            model_name='tag',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(blank=True, editable=False, help_text='A label for URL config.', populate_from=['name']),
        ),
    ]
