# Generated by Django 2.1.5 on 2019-05-12 04:12

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_auto_20190512_0505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 12, 4, 12, 39, 47281, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 12, 4, 12, 39, 46548, tzinfo=utc)),
        ),
    ]
