# Generated by Django 3.2.9 on 2021-11-28 18:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0015_projectrating'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projectrating',
            old_name='user_id',
            new_name='user',
        ),
    ]
