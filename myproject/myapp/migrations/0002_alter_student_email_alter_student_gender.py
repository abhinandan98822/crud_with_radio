# Generated by Django 4.1 on 2022-08-21 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=60, unique=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(max_length=1),
        ),
    ]
