# Generated by Django 3.1.4 on 2020-12-24 12:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='phone',
            old_name='type_id',
            new_name='type',
        ),
        migrations.RenameField(
            model_name='phone',
            old_name='user_id',
            new_name='user',
        ),
    ]
