# Generated by Django 2.0.2 on 2019-01-30 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fichas', '0012_auto_20190129_1023'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventario',
            name='media',
            field=models.DecimalField(decimal_places=2, max_digits=4, null=True),
        ),
    ]
