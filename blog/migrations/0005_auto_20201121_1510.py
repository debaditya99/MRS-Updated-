# Generated by Django 3.1.3 on 2020-11-21 09:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20201121_1313'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='dlike',
        ),
        migrations.RemoveField(
            model_name='post',
            name='like',
        ),
    ]
