# Generated by Django 2.2 on 2019-06-11 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='CreationTime',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='author',
            field=models.CharField(default='Name', max_length=30),
        ),
    ]
