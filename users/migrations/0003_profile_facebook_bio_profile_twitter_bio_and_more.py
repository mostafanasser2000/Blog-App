# Generated by Django 4.2.4 on 2023-10-16 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_about'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='facebook_bio',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='twitter_bio',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='youtube_bio',
            field=models.URLField(blank=True, null=True),
        ),
    ]
