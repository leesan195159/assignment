# Generated by Django 4.0.3 on 2022-03-16 10:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actormovie',
            name='actor',
        ),
        migrations.RemoveField(
            model_name='actormovie',
            name='movie',
        ),
        migrations.DeleteModel(
            name='Actor',
        ),
        migrations.DeleteModel(
            name='ActorMovie',
        ),
        migrations.DeleteModel(
            name='Movie',
        ),
    ]
