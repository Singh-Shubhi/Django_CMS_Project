# Generated by Django 4.2.3 on 2023-11-02 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ADMIN1APP', '0008_alter_doctor_contact_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deal',
            name='quantity_ordered',
            field=models.IntegerField(),
        ),
    ]