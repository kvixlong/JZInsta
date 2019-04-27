# Generated by Django 2.2 on 2019-04-25 00:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0008_auto_20190424_2247'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userconnection',
            name='followers',
        ),
        migrations.RemoveField(
            model_name='userconnection',
            name='instaUser',
        ),
        migrations.AddField(
            model_name='userconnection',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userconnection',
            name='creator',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='friendship_creator_set', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='userconnection',
            name='following',
        ),
        migrations.AddField(
            model_name='userconnection',
            name='following',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='friend_set', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]