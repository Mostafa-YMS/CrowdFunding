# Generated by Django 3.2.9 on 2021-12-03 18:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_rename_extra_data_userinfo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='user',
        ),
        migrations.DeleteModel(
            name='Reg',
        ),
        migrations.DeleteModel(
            name='Userinfo',
        ),
    ]
