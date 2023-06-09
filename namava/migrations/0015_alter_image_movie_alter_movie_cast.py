# Generated by Django 4.2 on 2023-04-09 11:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("namava", "0014_alter_movie_cast"),
    ]

    operations = [
        migrations.AlterField(
            model_name="image",
            name="movie",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="namava.movie"
            ),
        ),
        migrations.AlterField(
            model_name="movie",
            name="cast",
            field=models.ManyToManyField(to="namava.cast"),
        ),
    ]
