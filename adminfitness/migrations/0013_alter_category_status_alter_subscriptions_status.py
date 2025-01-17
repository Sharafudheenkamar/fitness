# Generated by Django 5.0.3 on 2024-04-07 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminfitness', '0012_alter_category_status_alter_subscriptions_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='status',
            field=models.CharField(blank=True, choices=[('ACTIVE', 'Active'), ('DEACTIVE', 'Deactive')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='subscriptions',
            name='status',
            field=models.CharField(blank=True, choices=[('ACTIVE', 'Active'), ('DEACTIVE', 'Deactive')], max_length=20, null=True),
        ),
    ]
