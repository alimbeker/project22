# Generated by Django 4.0.2 on 2022-03-17 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_sport_delete_articles_delete_doctors_delete_money_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenPrize',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullnames', models.CharField(max_length=50)),
                ('medaltype', models.CharField(max_length=50)),
            ],
        ),
    ]
