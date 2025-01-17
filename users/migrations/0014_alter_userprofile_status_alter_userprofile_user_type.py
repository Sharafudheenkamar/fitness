# Generated by Django 5.0.3 on 2024-04-07 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_alter_userprofile_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='status',
            field=models.CharField(blank=True, choices=[('ACTIVE', 'Active'), ('DEACTIVE', 'Deactive')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user_type',
            field=models.CharField(blank=True, choices=[('ADMIN', 'admin'), ('CLIENT', 'client'), ('TRAINER', 'trainer')], max_length=30, null=True),
        ),
    ]
