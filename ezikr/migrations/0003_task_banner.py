# Generated by Django 4.0.3 on 2022-09-29 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ezikr', '0002_ztype_alter_task_ztype'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='banner',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
