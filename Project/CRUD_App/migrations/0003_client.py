# Generated by Django 3.1.4 on 2020-12-12 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRUD_App', '0002_auto_20201211_1629'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('telephone', models.IntegerField()),
                ('email', models.CharField(max_length=120)),
                ('password', models.CharField(max_length=220)),
            ],
        ),
    ]