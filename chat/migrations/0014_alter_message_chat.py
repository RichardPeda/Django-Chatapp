# Generated by Django 5.1 on 2024-09-05 20:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0013_remove_chat_members_chat_author_chat_receiver_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='chat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chat_message_set', to='chat.chat'),
        ),
    ]
