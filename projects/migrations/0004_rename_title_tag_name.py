# Generated by Django 4.1.4 on 2022-12-13 21:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0003_rename_name_tag_title"),
    ]

    operations = [
        migrations.RenameField(
            model_name="tag",
            old_name="title",
            new_name="name",
        ),
    ]
