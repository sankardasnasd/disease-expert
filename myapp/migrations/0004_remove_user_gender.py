# Generated by Django 5.0.2 on 2024-02-29 04:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_remove_symptoms_symtoms_symptoms_symptoms'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='gender',
        ),
    ]