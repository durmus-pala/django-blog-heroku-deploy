# Generated by Django 3.2.5 on 2021-07-31 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0002_alter_post_last_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='last_updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]