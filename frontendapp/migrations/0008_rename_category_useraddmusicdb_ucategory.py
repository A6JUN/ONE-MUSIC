# Generated by Django 4.2.4 on 2023-12-14 06:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontendapp', '0007_rename_cname_useraddmusicdb_ucname_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='useraddmusicdb',
            old_name='category',
            new_name='ucategory',
        ),
    ]
