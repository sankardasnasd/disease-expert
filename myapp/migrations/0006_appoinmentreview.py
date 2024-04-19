# Generated by Django 5.0.2 on 2024-03-29 12:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_diease_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppoinmentReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Review', models.CharField(max_length=1000)),
                ('Rating', models.FloatField()),
                ('date', models.DateField()),
                ('APPOINTMENT', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.appointment')),
                ('USER', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.user')),
            ],
        ),
    ]