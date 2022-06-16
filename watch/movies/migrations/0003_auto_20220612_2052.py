# Generated by Django 3.1.6 on 2022-06-12 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_review_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='watchlist',
            name='avg_rating',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='watchlist',
            name='number_of_reviews',
            field=models.IntegerField(default=0),
        ),
    ]
