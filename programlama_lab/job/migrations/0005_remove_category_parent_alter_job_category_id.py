# Generated by Django 4.1.4 on 2022-12-24 12:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("job", "0004_category_slug_alter_category_title"),
    ]

    operations = [
        migrations.RemoveField(model_name="category", name="parent",),
        migrations.AlterField(
            model_name="job",
            name="category_id",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="job.category",
            ),
        ),
    ]