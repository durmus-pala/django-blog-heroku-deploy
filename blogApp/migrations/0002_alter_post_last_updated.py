# Generated by Django 3.2.5 on 2021-07-31 12:58

from django.db import migrations, models
import django.forms.utils


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='last_updated',
            field=models.DateTimeField(default=django.forms.utils.to_current_timezone),
        ),
    ]
