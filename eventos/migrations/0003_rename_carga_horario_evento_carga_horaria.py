# Generated by Django 4.2 on 2023-04-11 23:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0002_evento_criador'),
    ]

    operations = [
        migrations.RenameField(
            model_name='evento',
            old_name='carga_horario',
            new_name='carga_horaria',
        ),
    ]
