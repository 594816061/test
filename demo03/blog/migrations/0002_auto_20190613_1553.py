# Generated by Django 2.2.2 on 2019-06-13 07:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='creat_time',
            new_name='create_time',
        ),
    ]
