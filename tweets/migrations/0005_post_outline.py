# Generated by Django 3.0 on 2020-05-06 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0004_auto_20200506_0828'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='outline',
            field=models.TextField(blank=True, help_text='Optional, just helps'),
        ),
    ]
