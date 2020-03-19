# Generated by Django 3.0.4 on 2020-03-18 14:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('actor_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('F', 'female'), ('M', 'male')], max_length=1, null=True)),
                ('age', models.IntegerField(null=True)),
                ('fb_likes', models.IntegerField(null=True)),
                ('discription', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Cast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=50)),
                ('remuneration', models.FloatField(null=True)),
                ('is_debut_movie', models.BooleanField(default=False)),
                ('actor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='imdb.Actor')),
            ],
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('gender', models.CharField(choices=[('F', 'female'), ('M', 'male')], max_length=1, null=True)),
                ('age', models.IntegerField(null=True)),
                ('fb_likes', models.IntegerField(null=True)),
                ('discription', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('movie_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('release_year', models.CharField(max_length=10, null=True)),
                ('fb_likes', models.IntegerField(null=True)),
                ('average_rating', models.FloatField(null=True)),
                ('country', models.CharField(max_length=50, null=True)),
                ('language', models.CharField(max_length=50, null=True)),
                ('no_of_users_voted', models.IntegerField(null=True)),
                ('box_office_collection_in_crores', models.FloatField()),
                ('budget', models.FloatField(null=True)),
                ('discription', models.TextField(blank=True, null=True)),
                ('genre', models.CharField(max_length=50, null=True)),
                ('result', models.CharField(choices=[('Block Buster', 'B'), ('Average', 'A'), ('Disaster', 'D')], max_length=30, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('actors', models.ManyToManyField(through='imdb.Cast', to='imdb.Actor')),
                ('director', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='imdb.Director')),
            ],
        ),
        migrations.AddField(
            model_name='cast',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='imdb.Movie'),
        ),
    ]
