# Generated by Django 3.1.3 on 2020-11-21 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20201121_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='name',
            field=models.CharField(default=None, max_length=34),
        ),
    ]