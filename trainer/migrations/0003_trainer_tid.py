# Generated by Django 5.0.3 on 2024-03-30 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainer', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainer',
            name='tid',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
