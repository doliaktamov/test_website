# Generated by Django 3.2 on 2022-05-13 21:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qwe', '0003_auto_20220513_2129'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='result',
            name='category',
        ),
    ]