# Generated by Django 4.0.1 on 2022-01-09 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_remove_user_profile_id_remove_user_profile_token_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_profile',
            name='username',
            field=models.CharField(default='usern', max_length=30),
        ),
    ]
