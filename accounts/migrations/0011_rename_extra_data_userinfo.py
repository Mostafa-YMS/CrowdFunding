# Generated by Django 3.2.9 on 2021-11-30 20:18

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0010_extra_data'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='extra_data',
            new_name='Userinfo',
        ),
    ]
