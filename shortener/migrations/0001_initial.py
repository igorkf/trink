# Generated by Django 3.2.5 on 2021-07-04 19:03

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200)),
                ('created_by', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2021, 7, 4, 19, 3, 45, 839829, tzinfo=utc), editable=False)),
                ('expires_at', models.DateTimeField(default=datetime.datetime(2021, 7, 11, 19, 3, 45, 839853, tzinfo=utc), editable=False)),
                ('expired', models.BooleanField(default=False, editable=False)),
            ],
        ),
    ]
