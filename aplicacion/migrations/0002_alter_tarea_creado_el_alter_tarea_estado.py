# Generated by Django 4.1.7 on 2023-04-17 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarea',
            name='creado_el',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='tarea',
            name='estado',
            field=models.TextField(max_length=100),
        ),
    ]
