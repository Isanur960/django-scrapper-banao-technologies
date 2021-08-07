# Generated by Django 3.2.6 on 2021-08-06 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductDB',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=80)),
                ('link', models.TextField()),
                ('img', models.TextField()),
                ('price', models.CharField(max_length=20)),
                ('detail', models.TextField()),
            ],
        ),
    ]
