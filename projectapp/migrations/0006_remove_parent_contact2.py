# Generated by Django 4.0.1 on 2022-03-07 14:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp', '0005_alter_child_dateofbirth'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parent',
            name='contact2',
        ),
    ]
