# Generated by Django 3.2.5 on 2021-07-25 09:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Docs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=100)),
                ('number', models.IntegerField()),
                ('note', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frist_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('salary', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('bio', models.TextField()),
                ('photo', models.ImageField(blank=True, null=True, upload_to='clients_photo')),
                ('doc', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='clientes.docs')),
            ],
        ),
    ]
