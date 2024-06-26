# Generated by Django 2.2 on 2019-07-08 18:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('logbook', '0006_auto_20190708_1826'),
    ]

    operations = [
        migrations.CreateModel(
            name='LogBookEntry',
            fields=[
                ('SerialNumber', models.AutoField(primary_key=True, serialize=False)),
                ('CreatedAt', models.DateField(default=django.utils.timezone.now)),
                ('Author', models.TextField(max_length=30)),
                ('Designation', models.TextField(max_length=30)),
                ('Subject', models.TextField(max_length=300)),
                ('ReportedTo', models.TextField(max_length=40)),
                ('InstructedBy', models.TextField(max_length=40)),
            ],
        ),
        migrations.DeleteModel(
            name='LogBook',
        ),
    ]
