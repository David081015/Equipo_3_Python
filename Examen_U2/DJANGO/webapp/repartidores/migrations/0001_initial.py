# Generated by Django 4.2 on 2023-04-20 12:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paquete',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empresa', models.CharField(max_length=255)),
                ('peso', models.IntegerField()),
                ('pais', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Repartidor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('apellido', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('paquete', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='repartidores.paquete')),
            ],
        ),
    ]
