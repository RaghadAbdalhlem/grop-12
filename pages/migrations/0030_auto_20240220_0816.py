# Generated by Django 3.1.13 on 2024-02-20 06:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0029_catigoryclasses_privatesoftwarclasses'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='privatechemicalclasses',
            name='departmentcours',
        ),
        migrations.RemoveField(
            model_name='privatecivilclasses',
            name='departmentcours',
        ),
        migrations.RemoveField(
            model_name='privateelectricclasses',
            name='departmentcours',
        ),
        migrations.RemoveField(
            model_name='privatemechanicalclasses',
            name='departmentcours',
        ),
        migrations.RemoveField(
            model_name='privatesoftwarclasses',
            name='departmentcours',
        ),
    ]
