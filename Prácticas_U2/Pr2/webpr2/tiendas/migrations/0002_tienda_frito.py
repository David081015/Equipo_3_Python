# Generated by Django 4.1.7 on 2023-03-31 15:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tiendas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tienda',
            name='frito',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tiendas.frito'),
        ),
    ]
