# Generated by Django 2.2 on 2019-04-24 16:09

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0004_remove_post_plain_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to='static/images'),
        ),
    ]