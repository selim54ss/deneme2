# Generated by Django 4.1.4 on 2022-12-21 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("job", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="job",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to=""),
        ),
    ]
