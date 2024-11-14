# Generated by Django 5.0.3 on 2024-04-02 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainer', '0008_posture_likes_alter_posture_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posture',
            name='status',
            field=models.CharField(blank=True, choices=[('ACTIVE', 'Active'), ('DEACTIVE', 'Deactive')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='status',
            field=models.CharField(blank=True, choices=[('ACTIVE', 'Active'), ('DEACTIVE', 'Deactive')], max_length=20, null=True),
        ),
    ]
