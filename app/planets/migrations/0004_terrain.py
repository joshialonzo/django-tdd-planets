# Generated by Django 4.1.7 on 2024-07-23 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planets', '0003_alter_planet_population'),
    ]

    operations = [
        migrations.CreateModel(
            name='Terrain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
    ]
