# Generated by Django 5.1.2 on 2024-12-03 20:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_model', '0003_rename_user_userprofile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]