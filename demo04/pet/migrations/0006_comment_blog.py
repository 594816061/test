# Generated by Django 2.2.2 on 2019-06-20 06:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0005_auto_20190620_1438'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='blog',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='pet.Blog'),
        ),
    ]