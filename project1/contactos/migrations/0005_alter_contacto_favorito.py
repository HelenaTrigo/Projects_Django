# Generated by Django 5.0.1 on 2024-02-02 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactos', '0004_alter_contacto_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacto',
            name='favorito',
            field=models.BooleanField(default=False),
        ),
    ]
