# Generated by Django 5.0.3 on 2024-03-30 10:17

import django.db.models.deletion
import trainer.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainer', '0003_trainer_tid'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='trainer',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='posture',
            name='image',
            field=models.ImageField(blank=True, max_length=1000, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='posture',
            name='status',
            field=models.CharField(blank=True, choices=[('DEACTIVE', 'Deactive'), ('ACTIVE', 'Active')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='certificate',
            field=models.FileField(blank=True, null=True, upload_to=trainer.models.generate_unique_filename),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='status',
            field=models.CharField(blank=True, choices=[('DEACTIVE', 'Deactive'), ('ACTIVE', 'Active')], max_length=20, null=True),
        ),
    ]
