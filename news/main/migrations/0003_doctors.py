# Generated by Django 4.0.2 on 2022-03-16 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_veteran'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('Surname', models.CharField(max_length=200)),
                ('Proffesion', models.CharField(max_length=200)),
                ('about_doctor', models.CharField(max_length=500)),
                ('email', models.EmailField(max_length=200)),
            ],
        ),
    ]
