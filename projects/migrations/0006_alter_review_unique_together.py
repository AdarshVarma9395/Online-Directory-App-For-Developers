# Generated by Django 5.0.6 on 2024-11-15 06:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0005_alter_project_options_review_owner"),
        ("users", "0004_alter_profile_options"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="review",
            unique_together={("owner", "project")},
        ),
    ]
