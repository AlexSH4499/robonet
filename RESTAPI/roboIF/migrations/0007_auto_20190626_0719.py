# Generated by Django 2.2.2 on 2019-06-26 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roboIF', '0006_auto_20190625_0715'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='robot',
            options={'ordering': ['uid', 'name']},
        ),
        migrations.AddField(
            model_name='robot',
            name='ip_address',
            field=models.CharField(default='192.164.1.42', max_length=15),
        ),
    ]
