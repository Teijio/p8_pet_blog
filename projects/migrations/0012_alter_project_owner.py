# Generated by Django 4.1.4 on 2022-12-23 01:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0004_alter_profile_options"),
        ("projects", "0011_delete_message"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="owner",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="users.profile",
            ),
        ),
    ]
