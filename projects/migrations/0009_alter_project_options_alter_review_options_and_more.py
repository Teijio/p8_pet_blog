# Generated by Django 4.1.4 on 2022-12-20 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0008_review_owner_alter_review_unique_together"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="project",
            options={"ordering": ("-vote_ratio", "-vote_total", "-created")},
        ),
        migrations.AlterModelOptions(
            name="review",
            options={"ordering": ("-created",)},
        ),
        migrations.AlterField(
            model_name="review",
            name="value",
            field=models.TextField(
                choices=[("up", "Up vote"), ("down", "Down vote")], max_length=200
            ),
        ),
    ]
