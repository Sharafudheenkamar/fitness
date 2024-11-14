# Generated by Django 5.0.3 on 2024-04-05 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0013_alter_bank_status_alter_chat_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bank',
            name='status',
            field=models.CharField(blank=True, choices=[('DEACTIVE', 'Deactive'), ('ACTIVE', 'Active')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='chat',
            name='status',
            field=models.CharField(blank=True, choices=[('DEACTIVE', 'Deactive'), ('ACTIVE', 'Active')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='clientprofile',
            name='status',
            field=models.CharField(blank=True, choices=[('DEACTIVE', 'Deactive'), ('ACTIVE', 'Active')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='status',
            field=models.CharField(blank=True, choices=[('DEACTIVE', 'Deactive'), ('ACTIVE', 'Active')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='status',
            field=models.CharField(blank=True, choices=[('DEACTIVE', 'Deactive'), ('ACTIVE', 'Active')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='status',
            field=models.CharField(blank=True, choices=[('DEACTIVE', 'Deactive'), ('ACTIVE', 'Active')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='rating',
            name='status',
            field=models.CharField(blank=True, choices=[('DEACTIVE', 'Deactive'), ('ACTIVE', 'Active')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='videocomment',
            name='status',
            field=models.CharField(blank=True, choices=[('DEACTIVE', 'Deactive'), ('ACTIVE', 'Active')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='videolike',
            name='status',
            field=models.CharField(blank=True, choices=[('DEACTIVE', 'Deactive'), ('ACTIVE', 'Active')], max_length=20, null=True),
        ),
    ]
