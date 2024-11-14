# Generated by Django 5.0.3 on 2024-04-07 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainer', '0016_alter_challenges_status_alter_diet_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challenges',
            name='status',
            field=models.CharField(blank=True, choices=[('ACTIVE', 'Active'), ('DEACTIVE', 'Deactive')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='diet',
            name='file',
            field=models.FileField(blank=True, max_length=500, null=True, upload_to='diet_files/'),
        ),
        migrations.AlterField(
            model_name='diet',
            name='status',
            field=models.CharField(blank=True, choices=[('ACTIVE', 'Active'), ('DEACTIVE', 'Deactive')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='posture',
            name='status',
            field=models.CharField(blank=True, choices=[('ACTIVE', 'Active'), ('DEACTIVE', 'Deactive')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(blank=True, choices=[('ACTIVE', 'Active'), ('DEACTIVE', 'Deactive')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='status',
            field=models.CharField(blank=True, choices=[('ACTIVE', 'Active'), ('DEACTIVE', 'Deactive')], max_length=20, null=True),
        ),
    ]