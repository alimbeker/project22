# Generated by Django 4.0.2 on 2022-04-14 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_mvideo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('confirmpassword', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=1)),
            ],
        ),
    ]