# Generated by Django 3.0.4 on 2020-03-19 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imdb', '0004_auto_20200319_0157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='fb_likes',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='director',
            name='fb_likes',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='fb_likes',
            field=models.IntegerField(null=True),
        ),
    ]
