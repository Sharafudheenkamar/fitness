# Generated by Django 5.0.3 on 2024-04-15 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0027_alter_userprofile_subscriptionplan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='subscriptionplan',
            field=models.CharField(blank=True, choices=[('STANDARD', 'standard'), ('ORDINARY', 'ordinary'), ('PREMIUM', 'premium')], default='ORDINARY', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user_type',
            field=models.CharField(blank=True, choices=[('TRAINER', 'trainer'), ('ADMIN', 'admin'), ('CLIENT', 'client')], max_length=30, null=True),
        ),
    ]
