# Generated by Django 4.0.1 on 2022-03-04 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='parent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=8)),
                ('nationality', models.CharField(max_length=20)),
                ('dateofbirth', models.CharField(max_length=30)),
                ('occupation', models.CharField(max_length=20)),
                ('Address', models.CharField(max_length=50)),
                ('contact1', models.IntegerField(max_length=12)),
                ('contact2', models.IntegerField(max_length=12)),
                ('email', models.EmailField(max_length=20)),
                ('motivation', models.CharField(max_length=100)),
            ],
        ),
    ]
