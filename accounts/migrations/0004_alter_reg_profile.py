# Generated by Django 3.2.9 on 2021-11-25 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_reg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reg',
            name='profile',
            field=models.ImageField(default=None, height_field=200, upload_to='', width_field=200),
        ),
    ]
