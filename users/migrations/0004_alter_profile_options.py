# Generated by Django 4.1.4 on 2022-12-23 01:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_message"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="profile",
            options={"ordering": ("created",)},
        ),
    ]