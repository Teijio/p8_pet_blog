# Generated by Django 4.1.4 on 2022-12-13 21:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0002_tag_project_vote_ratio_project_vote_total_review_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="tag",
            old_name="name",
            new_name="title",
        ),
    ]