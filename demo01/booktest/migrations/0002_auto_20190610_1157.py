# Generated by Django 2.2.2 on 2019-06-10 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='heroinfo',
            name='gender',
            field=models.CharField(blank=True, choices=[('man', '男'), ('woman', '女')], max_length=5, null=True),
        ),
    ]