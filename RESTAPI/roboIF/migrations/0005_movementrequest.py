# Generated by Django 2.2.2 on 2019-06-25 14:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('roboIF', '0004_auto_20190624_1316'),
    ]

    operations = [
        migrations.CreateModel(
            name='MovementRequest',
            fields=[
                ('uid', models.IntegerField(primary_key=True, serialize=False)),
                ('joint_1', models.DecimalField(decimal_places=2, max_digits=6)),
                ('joint_2', models.DecimalField(decimal_places=2, max_digits=6)),
                ('joint_3', models.DecimalField(decimal_places=2, max_digits=6)),
                ('joint_4', models.DecimalField(decimal_places=2, max_digits=6)),
                ('joint_5', models.DecimalField(decimal_places=2, max_digits=6)),
                ('joint_6', models.DecimalField(decimal_places=2, max_digits=6)),
                ('robot_to_send', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='roboIF.Robot')),
            ],
            options={
                'ordering': ['uid', 'robot_to_send'],
            },
        ),
    ]