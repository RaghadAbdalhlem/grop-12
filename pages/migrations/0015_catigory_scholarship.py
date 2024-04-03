# Generated by Django 3.1.13 on 2024-02-17 12:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0014_auto_20240216_2200'),
    ]

    operations = [
        migrations.CreateModel(
            name='Catigory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='scholarship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contant', models.CharField(max_length=1000)),
                ('category', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='pages.catigory')),
            ],
        ),
    ]
