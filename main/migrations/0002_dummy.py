# Generated by Django 3.1.7 on 2021-05-03 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='dummy',
            fields=[
                ('des', models.CharField(max_length=70)),
                ('imag_url', models.CharField(max_length=512)),
                ('linkA', models.CharField(max_length=1070)),
                ('linkF', models.CharField(max_length=1070)),
                ('linkC', models.CharField(max_length=1070)),
                ('amazonP', models.IntegerField()),
                ('flipkartP', models.IntegerField()),
                ('cromaP', models.IntegerField()),
            ],
        ),
    ]
