# Generated by Django 3.1.4 on 2020-12-10 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('subtitle', models.CharField(max_length=220)),
                ('description', models.TextField(max_length=500)),
                ('dataTiem', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]