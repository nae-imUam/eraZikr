# Generated by Django 4.0.3 on 2022-09-29 22:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80, null=True)),
                ('ztype', models.CharField(max_length=50, null=True)),
                ('script', models.CharField(max_length=250, null=True)),
                ('iloc', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Challange',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ezikr.task')),
            ],
        ),
    ]
