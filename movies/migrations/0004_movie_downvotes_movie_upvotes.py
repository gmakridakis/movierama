# Generated by Django 4.0.3 on 2022-03-12 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_vote'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='downvotes',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='movie',
            name='upvotes',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
