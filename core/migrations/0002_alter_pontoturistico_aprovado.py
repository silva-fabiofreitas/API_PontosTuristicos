# Generated by Django 4.0.2 on 2022-02-19 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pontoturistico',
            name='aprovado',
            field=models.BooleanField(default=False),
        ),
    ]
