# Generated by Django 2.2.2 on 2019-06-25 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roboIF', '0005_movementrequest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='warehouse',
            name='uid',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
    ]
