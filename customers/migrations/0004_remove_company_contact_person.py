# Generated by Django 4.1.6 on 2023-02-06 15:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0003_remove_company_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='contact_person',
        ),
    ]
