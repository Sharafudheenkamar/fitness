# Generated by Django 5.0.3 on 2024-04-04 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminfitness', '0005_alter_category_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='status',
            field=models.CharField(blank=True, choices=[('DEACTIVE', 'Deactive'), ('ACTIVE', 'Active')], max_length=20, null=True),
        ),
    ]
