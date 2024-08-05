# Generated by Django 5.0.7 on 2024-07-14 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('selling_price', models.FloatField()),
                ('discount_price', models.FloatField()),
                ('description', models.TextField()),
                ('composition', models.TextField(default='')),
                ('prodapp', models.TextField(default='')),
                ('category', models.CharField(choices=[('CP', 'Capsicum'), ('CR', 'Carrot'), ('CF', 'Cauliflower'), ('CL', 'Corianderleaves'), ('BW', 'Babywipes'), ('BA', 'Babywipes'), ('CP', 'Capsicum'), ('CR', 'Carrot'), ('CF', 'Cauliflower'), ('CL', 'Corianderleaves'), ('BW', 'Babywipes'), ('BA', 'Babywipes')], max_length=2)),
                ('product_image', models.ImageField(upload_to='product')),
            ],
        ),
    ]
