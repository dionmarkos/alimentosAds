# Generated by Django 2.0.13 on 2019-06-12 18:35

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('aulas', '0005_auto_20190612_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aula',
            name='data',
            field=models.DateField(default=datetime.datetime(2019, 6, 12, 18, 35, 29, 163356, tzinfo=utc)),
        ),
    ]