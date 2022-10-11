# Generated by Django 4.1.1 on 2022-10-09 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='statslist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Symbol', models.CharField(max_length=200)),
                ('Last', models.CharField(max_length=200)),
                ('Change', models.CharField(max_length=200)),
                ('Changeperc', models.CharField(max_length=200)),
                ('Close', models.CharField(max_length=200)),
                ('High', models.CharField(max_length=200)),
                ('Low', models.CharField(max_length=200)),
                ('LastTrade', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='stats',
        ),
    ]
