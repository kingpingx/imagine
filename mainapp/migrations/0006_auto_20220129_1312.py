# Generated by Django 2.2.10 on 2022-01-29 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_alter_user_profile_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_profile',
            name='image',
        ),
        migrations.AddField(
            model_name='user_profile',
            name='path',
            field=models.CharField(default='one', max_length=60),
        ),
        migrations.AlterField(
            model_name='user_profile',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('rather not to say', 'Rather not to say')], default='select', max_length=20),
        ),
        migrations.AlterField(
            model_name='user_profile',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='user_profile',
            name='ph_number',
            field=models.IntegerField(),
        ),
    ]
