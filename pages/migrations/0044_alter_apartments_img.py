# Generated by Django 5.0.2 on 2024-02-25 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0043_alter_apartments_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartments',
            name='img',
            field=models.ImageField(upload_to='static/image/'),
        ),
    ]