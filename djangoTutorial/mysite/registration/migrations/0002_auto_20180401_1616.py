# Generated by Django 2.0.3 on 2018-04-01 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voter',
            name='voted_for_Curr',
            field=models.BooleanField(default=0),
        ),
    ]
