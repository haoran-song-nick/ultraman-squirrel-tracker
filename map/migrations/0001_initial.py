# Generated by Django 3.0.7 on 2020-10-19 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Point',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Unique_Squirrel_ID', models.CharField(help_text='Unique Squirrel ID', max_length=100, unique=True)),
                ('Latitude', models.FloatField(help_text='Latitude')),
                ('Longtitude', models.FloatField(help_text='Longtitude')),
            ],
        ),
    ]
