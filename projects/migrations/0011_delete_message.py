# Generated by Django 4.1.4 on 2022-12-20 20:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0010_alter_review_value_message"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Message",
        ),
    ]