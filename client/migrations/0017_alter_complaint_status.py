# Generated by Django 5.0.3 on 2024-04-07 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0016_alter_bank_status_alter_chat_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='status',
            field=models.CharField(blank=True, default='pending', max_length=20, null=True),
        ),
    ]
