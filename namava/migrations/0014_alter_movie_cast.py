# Generated by Django 4.2 on 2023-04-09 09:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("namava", "0013_movie_director"),
    ]

    operations = [
        migrations.AlterField(
            model_name="movie",
            name="cast",
            field=models.ManyToManyField(related_name="movie", to="namava.cast"),
        ),
    ]
