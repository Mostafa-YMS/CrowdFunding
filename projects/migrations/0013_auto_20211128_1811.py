# Generated by Django 3.2.9 on 2021-11-28 18:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0012_alter_projectimages_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projecttags',
            name='project',
        ),
        migrations.DeleteModel(
            name='ProjectImages',
        ),
        migrations.DeleteModel(
            name='Projects',
        ),
        migrations.DeleteModel(
            name='ProjectTags',
        ),
    ]
