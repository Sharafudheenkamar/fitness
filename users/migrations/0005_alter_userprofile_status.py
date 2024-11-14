# Generated by Django 5.0.3 on 2024-04-02 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_userprofile_status_alter_userprofile_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='status',
            field=models.CharField(blank=True, choices=[('ACTIVE', 'Active'), ('DEACTIVE', 'Deactive')], max_length=20, null=True),
        ),
    ]
