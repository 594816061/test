# Generated by Django 2.2.2 on 2019-06-20 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0002_about_recommend_slideshow_welcome'),
    ]

    operations = [
        migrations.CreateModel(
            name='HintTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic', models.ImageField(upload_to='hint_pic')),
                ('hint', models.CharField(max_length=30)),
            ],
        ),
    ]
