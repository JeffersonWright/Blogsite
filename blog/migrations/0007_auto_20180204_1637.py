# Generated by Django 2.0.1 on 2018-02-05 00:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20180204_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='post',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
