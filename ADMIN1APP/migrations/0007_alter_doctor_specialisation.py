# Generated by Django 4.2.3 on 2023-08-07 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ADMIN1APP', '0006_alter_product1_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='specialisation',
            field=models.CharField(max_length=200),
        ),
    ]