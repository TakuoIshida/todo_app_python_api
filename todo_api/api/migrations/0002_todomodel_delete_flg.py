# Generated by Django 3.2 on 2021-04-24 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todomodel',
            name='delete_flg',
            field=models.BooleanField(default=False),
        ),
    ]