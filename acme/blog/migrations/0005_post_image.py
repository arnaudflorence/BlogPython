# Generated by Django 2.1 on 2018-08-22 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_remove_post_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.CharField(default='http://www.generation-voyageurs.com/wp-content/uploads/2017/08/2-plage-600x400.jpg', max_length=255),
        ),
    ]
