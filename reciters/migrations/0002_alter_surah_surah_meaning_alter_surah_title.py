# Generated by Django 4.1.1 on 2022-09-20 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reciters', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='surah',
            name='surah_meaning',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='surah',
            name='title',
            field=models.CharField(default='', max_length=220),
        ),
    ]
