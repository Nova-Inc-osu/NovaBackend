# Generated by Django 2.2.5 on 2019-11-07 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nova', '0003_auto_20191015_1535'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='analysis_value',
            field=models.FloatField(default=0),
        ),
    ]