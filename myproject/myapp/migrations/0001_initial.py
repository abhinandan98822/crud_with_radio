# Generated by Django 4.1 on 2022-08-21 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=30)),
                ('username', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=60)),
                ('password', models.CharField(max_length=60)),
                ('salary', models.IntegerField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
            ],
        ),
    ]
