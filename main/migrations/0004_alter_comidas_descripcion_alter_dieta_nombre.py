# Generated by Django 4.1.6 on 2023-03-22 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_dieta_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comidas',
            name='descripcion',
            field=models.TextField(max_length=100000),
        ),
        migrations.AlterField(
            model_name='dieta',
            name='nombre',
            field=models.TextField(max_length=1000),
        ),
    ]
