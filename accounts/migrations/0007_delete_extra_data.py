# Generated by Django 3.2.9 on 2021-11-30 19:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_extra_data'),
    ]

    operations = [
        migrations.DeleteModel(
            name='extra_data',
        ),
    ]
