# Generated by Django 4.0 on 2022-01-10 22:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_comment_alter_user_first_name_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
