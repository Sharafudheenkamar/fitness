# Generated by Django 5.0.3 on 2024-04-02 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminfitness', '0004_alter_category_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='status',
            field=models.CharField(blank=True, choices=[('ACTIVE', 'Active'), ('DEACTIVE', 'Deactive')], max_length=20, null=True),
        ),
    ]