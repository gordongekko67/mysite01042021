# Generated by Django 3.1.7 on 2021-03-06 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funzioni_iot', '0002_question'),
    ]

    operations = [
        migrations.CreateModel(
            name='Giornalista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20)),
                ('cognome', models.CharField(max_length=40)),
            ],
        ),
    ]
