# Generated by Django 4.2.5 on 2024-06-23 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient_details_tb',
            name='profile_path',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
