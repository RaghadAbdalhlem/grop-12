# Generated by Django 3.1.13 on 2024-02-15 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_private_classes'),
    ]

    operations = [
        migrations.AddField(
            model_name='private_classes',
            name='img',
            field=models.ImageField(default='static/image/personalclass.png', upload_to=''),
        ),
    ]
