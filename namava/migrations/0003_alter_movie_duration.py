# Generated by Django 4.2 on 2023-04-07 13:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("namava", "0002_alter_movie_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="movie",
            name="duration",
            field=models.IntegerField(),
        ),
    ]
