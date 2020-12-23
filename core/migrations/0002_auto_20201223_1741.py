# Generated by Django 3.1.4 on 2020-12-23 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='addresses',
            options={'verbose_name': 'Адрес', 'verbose_name_plural': 'Адреса'},
        ),
        migrations.AlterModelOptions(
            name='fio',
            options={'verbose_name': 'ФИО', 'verbose_name_plural': 'ФИО'},
        ),
        migrations.AlterModelOptions(
            name='phones',
            options={'verbose_name': 'Телефон', 'verbose_name_plural': 'Телефоны'},
        ),
        migrations.AlterField(
            model_name='addresses',
            name='address',
            field=models.TextField(max_length=64, verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='fio',
            name='father_name',
            field=models.TextField(max_length=16, verbose_name='Отчество'),
        ),
        migrations.AlterField(
            model_name='fio',
            name='first_name',
            field=models.TextField(max_length=16, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='fio',
            name='last_name',
            field=models.TextField(max_length=16, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='phones',
            name='phone',
            field=models.TextField(max_length=32, verbose_name='Номер телефона'),
        ),
        migrations.AlterField(
            model_name='type',
            name='type_name',
            field=models.TextField(max_length=16, verbose_name='Тип телефона'),
        ),
    ]
