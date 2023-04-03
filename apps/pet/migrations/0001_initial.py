# Generated by Django 4.1.7 on 2023-04-03 18:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shelter', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('age', models.CharField(max_length=10)),
                ('size', models.CharField(max_length=15)),
                ('characteristics', models.CharField(max_length=25)),
                ('shelter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shelter.shelter')),
            ],
        ),
    ]
