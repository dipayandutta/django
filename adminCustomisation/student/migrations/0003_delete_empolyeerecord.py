# Generated by Django 4.2.5 on 2024-05-26 15:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_empolyeerecord_alter_students_options'),
    ]

    operations = [
        migrations.DeleteModel(
            name='EmpolyeeRecord',
        ),
    ]
