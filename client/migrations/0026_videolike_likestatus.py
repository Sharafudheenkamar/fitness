# Generated by Django 5.0.3 on 2024-04-09 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0025_alter_bank_status_alter_chat_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='videolike',
            name='likestatus',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
