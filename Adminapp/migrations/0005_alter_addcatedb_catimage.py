# Generated by Django 4.2.4 on 2023-11-18 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Adminapp', '0004_addcatedb_catimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addcatedb',
            name='catimage',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]