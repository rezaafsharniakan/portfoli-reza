# Generated by Django 3.2.3 on 2022-05-07 09:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blogM', '0004_alter_comment_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='file',
            field=models.FileField(default=django.utils.timezone.now, upload_to='blogM/staticfile/'),
            preserve_default=False,
        ),
    ]
