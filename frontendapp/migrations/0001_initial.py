# Generated by Django 4.2.4 on 2023-11-18 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='signupdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('susername', models.CharField(blank=True, max_length=100, null=True)),
                ('semail', models.CharField(blank=True, max_length=100, null=True)),
                ('snumber', models.IntegerField(blank=True, null=True)),
                ('spassword', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]