# Generated by Django 5.0.3 on 2024-04-16 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0030_remove_bank_acholdername_bank_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='status',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
