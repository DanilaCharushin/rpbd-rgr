# Generated by Django 3.1.4 on 2020-12-24 12:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=16, verbose_name='Тип телефона')),
            ],
            options={
                'verbose_name': 'Тип',
                'verbose_name_plural': 'Типы',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.TextField(max_length=16, verbose_name='Имя')),
                ('last_name', models.TextField(max_length=16, verbose_name='Фамилия')),
                ('father_name', models.TextField(max_length=16, verbose_name='Отчество')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.TextField(max_length=32, verbose_name='Номер телефона')),
                ('type_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='phones', to='core.type', verbose_name='Тип')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='phones', to='core.user', verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Телефон',
                'verbose_name_plural': 'Телефоны',
            },
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=64, verbose_name='Адрес')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='address', to='core.user', verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Адрес',
                'verbose_name_plural': 'Адреса',
            },
        ),
    ]
