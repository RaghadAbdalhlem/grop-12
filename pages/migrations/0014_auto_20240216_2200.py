# Generated by Django 3.1.13 on 2024-02-16 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0013_auto_20240216_2129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='privatechemicalclasses',
            name='departmentcourse',
            field=models.CharField(default='CHEMICAL ENGINEERING', editable=False, max_length=50),
        ),
        migrations.AlterField(
            model_name='privatecivilclasses',
            name='departmentcourse',
            field=models.CharField(default='CIVIL ENGINEERING', editable=False, max_length=50),
        ),
        migrations.AlterField(
            model_name='privateelectricclasses',
            name='departmentcourse',
            field=models.CharField(default='ELECTRIC ENGINEERING', editable=False, max_length=50),
        ),
        migrations.AlterField(
            model_name='privatemechanicalclasses',
            name='departmentcourse',
            field=models.CharField(default='MECHANICAL ENGINEERING', editable=False, max_length=50),
        ),
        migrations.AlterField(
            model_name='privatesoftwarclasses',
            name='departmentcourse',
            field=models.CharField(default='SOFTWAR ENGINEERING', editable=False, max_length=50),
        ),
    ]