# Generated by Django 3.2.3 on 2022-04-11 05:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blogM', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='blogM/images/'),
            preserve_default=False,
        ),
    ]
