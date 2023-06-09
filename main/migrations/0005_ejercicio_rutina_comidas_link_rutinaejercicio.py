# Generated by Django 4.1.7 on 2023-04-23 22:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_comidas_descripcion_alter_dieta_nombre'),
    ]

    operations = [
        migrations.CreateModel(
            name='ejercicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField(max_length=50)),
                ('grupoMuscular', models.TextField(max_length=50)),
                ('descripcion', models.TextField(max_length=100000)),
                ('link', models.URLField(default=' ', max_length=4000)),
            ],
        ),
        migrations.CreateModel(
            name='rutina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField(max_length=1000)),
                ('descripcion', models.TextField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='comidas',
            name='link',
            field=models.URLField(default=' ', max_length=4000),
        ),
        migrations.CreateModel(
            name='rutinaEjercicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ejercicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.ejercicio')),
                ('rutina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.rutina')),
            ],
        ),
    ]
