# Generated by Django 5.1.6 on 2025-02-12 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('announcement', models.CharField(max_length=250, verbose_name='Announcement')),
                ('acticle', models.TextField(verbose_name='Article')),
                ('date', models.DateTimeField(verbose_name='Date of publish')),
            ],
        ),
    ]
