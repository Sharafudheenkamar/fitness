# Generated by Django 5.0.3 on 2024-04-07 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainer', '0017_alter_challenges_status_alter_diet_file_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challenges',
            name='status',
            field=models.CharField(blank=True, choices=[('DEACTIVE', 'Deactive'), ('ACTIVE', 'Active')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='challenges',
            name='video_file',
            field=models.FileField(blank=True, null=True, upload_to='challengefiles/'),
        ),
        migrations.AlterField(
            model_name='diet',
            name='status',
            field=models.CharField(blank=True, choices=[('DEACTIVE', 'Deactive'), ('ACTIVE', 'Active')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='posture',
            name='status',
            field=models.CharField(blank=True, choices=[('DEACTIVE', 'Deactive'), ('ACTIVE', 'Active')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(blank=True, choices=[('DEACTIVE', 'Deactive'), ('ACTIVE', 'Active')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='status',
            field=models.CharField(blank=True, choices=[('DEACTIVE', 'Deactive'), ('ACTIVE', 'Active')], max_length=20, null=True),
        ),
    ]