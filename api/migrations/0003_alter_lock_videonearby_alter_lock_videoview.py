# Generated by Django 4.0.2 on 2022-02-16 16:37

from django.db import migrations
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_lockimage_lock_alter_nearyby_lock_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lock',
            name='videoNearby',
            field=embed_video.fields.EmbedVideoField(),
        ),
        migrations.AlterField(
            model_name='lock',
            name='videoView',
            field=embed_video.fields.EmbedVideoField(),
        ),
    ]
