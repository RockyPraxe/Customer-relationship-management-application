# Generated by Django 3.2.22 on 2023-10-20 01:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crmapp', '0009_alter_customer_profile_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='profile_pic',
        ),
    ]
