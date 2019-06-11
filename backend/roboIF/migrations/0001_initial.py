# Generated by Django 2.2.2 on 2019-06-11 19:39

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Robot',
            fields=[
                ('uid', models.IntegerField(primary_key=True, serialize=False)),
                ('location', models.CharField(max_length=15)),
            ],
            options={
                'ordering': ['uid'],
            },
            managers=[
                ('robot_manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='WareHouse',
            fields=[
                ('uid', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('robots', models.ManyToManyField(to='roboIF.Robot')),
            ],
            options={
                'ordering': ['uid', 'name'],
            },
            managers=[
                ('manager', django.db.models.manager.Manager()),
            ],
        ),
    ]
