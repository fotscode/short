# Generated by Django 4.0.1 on 2022-01-10 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='url_short',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
