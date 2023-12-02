# Generated by Django 4.2.4 on 2023-12-01 16:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0002_alter_post_tags"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="tags",
            field=models.ManyToManyField(
                blank=True, related_name="tags", to="blog.tag"
            ),
        ),
    ]
