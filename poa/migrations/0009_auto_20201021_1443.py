# Generated by Django 2.2 on 2020-10-21 20:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poa', '0008_auto_20201021_1441'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inlinesalarioprogramatico',
            old_name='salario_pragmatico',
            new_name='salario_programatico',
        ),
    ]