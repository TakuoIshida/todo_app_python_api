# Generated by Django 3.2 on 2021-04-24 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_todomodel_delete_flg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todomodel',
            name='content',
            field=models.TextField(max_length=400),
        ),
        migrations.AlterField(
            model_name='todomodel',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]