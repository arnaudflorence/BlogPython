# Generated by Django 2.1 on 2018-08-24 12:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='Post_id',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
