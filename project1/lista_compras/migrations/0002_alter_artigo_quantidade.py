# Generated by Django 5.0.1 on 2024-02-02 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lista_compras', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artigo',
            name='quantidade',
            field=models.CharField(blank=True, default='1', max_length=20),
        ),
    ]
