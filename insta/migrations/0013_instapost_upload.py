# Generated by Django 2.2.1 on 2019-05-02 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0012_auto_20190502_1352'),
    ]

    operations = [
        migrations.AddField(
            model_name='instapost',
            name='upload',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]