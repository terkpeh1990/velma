# Generated by Django 4.1.6 on 2023-02-06 16:11

import django.contrib.postgres.fields.hstore
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0004_remove_company_contact_person'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='address',
            field=django.contrib.postgres.fields.hstore.HStoreField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='contact_person',
            field=django.contrib.postgres.fields.hstore.HStoreField(blank=True, null=True),
        ),
    ]
