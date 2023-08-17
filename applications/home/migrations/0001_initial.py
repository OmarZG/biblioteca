# Generated by Django 3.1.3 on 2020-11-30 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50, verbose_name='Nombres')),
                ('pais', models.CharField(max_length=50, verbose_name='Pais')),
                ('pasaporte', models.CharField(max_length=50, verbose_name='Pasaporte')),
                ('edad', models.PositiveIntegerField()),
                ('apelativo', models.CharField(max_length=10, verbose_name='Apelativo')),
            ],
            options={
                'verbose_name': 'Persona',
                'verbose_name_plural': 'Personas',
                'db_table': 'persona',
            },
        ),
    ]
