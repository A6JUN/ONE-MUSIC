# Generated by Django 4.2.4 on 2023-12-14 06:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontendapp', '0006_useraddmusicdb_alter_likedb_likmname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='useraddmusicdb',
            old_name='cname',
            new_name='ucname',
        ),
        migrations.RenameField(
            model_name='useraddmusicdb',
            old_name='description',
            new_name='udescription',
        ),
        migrations.RenameField(
            model_name='useraddmusicdb',
            old_name='image',
            new_name='uimage',
        ),
        migrations.RenameField(
            model_name='useraddmusicdb',
            old_name='music',
            new_name='umusic',
        ),
        migrations.RenameField(
            model_name='useraddmusicdb',
            old_name='mname',
            new_name='uname',
        ),
    ]