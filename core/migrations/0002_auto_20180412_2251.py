# Generated by Django 2.0.4 on 2018-04-12 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='name',
            field=models.CharField(max_length=160, unique=True, verbose_name='Name'),
        ),
    ]
