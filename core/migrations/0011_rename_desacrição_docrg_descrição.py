# Generated by Django 4.0.2 on 2022-03-17 00:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_rename_descrtion_docrg_desacrição'),
    ]

    operations = [
        migrations.RenameField(
            model_name='docrg',
            old_name='desacrição',
            new_name='descrição',
        ),
    ]
