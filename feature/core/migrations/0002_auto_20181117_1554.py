# Generated by Django 2.1.3 on 2018-11-17 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='priority',
        ),
        migrations.AddField(
            model_name='featurerequest',
            name='priority',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]