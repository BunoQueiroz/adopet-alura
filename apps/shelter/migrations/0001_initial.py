# Generated by Django 5.1.1 on 2024-09-18 11:37

import django.contrib.auth.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shelter',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('name', models.CharField(max_length=50)),
                ('borhood', models.CharField(blank=True, max_length=100)),
                ('city', models.CharField(max_length=70)),
                ('state', models.CharField(max_length=70)),
                ('phone', models.CharField(blank=True, max_length=18)),
                ('image', models.ImageField(blank=True, upload_to='shelters/%Y/%m/%d/')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
