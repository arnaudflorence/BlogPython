# Generated by Django 2.1 on 2018-08-29 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0024_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='slug',
        ),
    ]
