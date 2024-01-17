# Generated by Django 4.2.3 on 2023-08-02 06:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ADMIN1APP', '0004_appointment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity_ordered', models.PositiveIntegerField()),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ADMIN1APP.doctor')),
                ('entered_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ADMIN1APP.employee1')),
                ('product_name1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ADMIN1APP.product1')),
            ],
        ),
    ]