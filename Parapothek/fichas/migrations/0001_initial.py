# Generated by Django 2.0.2 on 2019-01-22 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inventario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('cn', models.TextField(blank=True, null=True)),
                ('nombre', models.TextField(blank=True, null=True)),
                ('pvf', models.TextField(blank=True, null=True)),
                ('pvp', models.TextField(blank=True, null=True)),
                ('stock', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Inventario',
                'managed': False,
            },
        ),
    ]