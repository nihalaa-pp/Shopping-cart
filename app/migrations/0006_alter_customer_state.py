# Generated by Django 5.0.7 on 2024-07-15 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='state',
            field=models.CharField(choices=[('TAMILNADU', 'TAMILNADU'), ('KERALA', 'KERALA'), ('GOA', 'GOA'), ('KARNATAKA', 'KARNATAKA')], max_length=100),
        ),
    ]
