# Generated by Django 5.1 on 2024-09-06 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0016_alter_message_receiver'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='male',
            field=models.BooleanField(default=True),
        ),
    ]
