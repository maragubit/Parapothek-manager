# Generated by Django 2.0.2 on 2019-02-02 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fichas', '0014_zona_indicaciones'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='zona',
            name='indicaciones',
        ),
        migrations.AddField(
            model_name='indicacion',
            name='zona',
            field=models.ManyToManyField(to='fichas.Zona'),
        ),
    ]
