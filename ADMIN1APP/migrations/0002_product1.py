# Generated by Django 4.2.3 on 2023-08-01 13:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ADMIN1APP', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('company_name', models.CharField(max_length=100)),
                ('product_image', models.ImageField(upload_to='media')),
                ('product_price', models.DecimalField(decimal_places=2, default=0, max_digits=50)),
                ('entered_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ADMIN1APP.employee1')),
            ],
        ),
    ]
