# Generated by Django 4.0.3 on 2022-09-29 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ezikr', '0007_alter_task_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='time',
            field=models.CharField(max_length=7, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(max_length=80, null=True),
        ),
    ]
