# Generated by Django 4.2.4 on 2023-12-02 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontendapp', '0003_likedb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='likedb',
            name='likmusic',
            field=models.FileField(blank=True, null=True, unique=True, upload_to='Music'),
        ),
    ]