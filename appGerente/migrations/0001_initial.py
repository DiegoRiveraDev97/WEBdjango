# Generated by Django 4.1 on 2022-09-16 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Heladeria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreHeladeria', models.CharField(max_length=100)),
                ('nombreGerente', models.CharField(max_length=100)),
                ('nitHeladeria', models.IntegerField(unique=True)),
                ('correoGerente', models.CharField(max_length=100)),
                ('cedulaGerente', models.IntegerField()),
                ('ubicacionHeladeria', models.CharField(max_length=200)),
            ],
        ),
    ]
