# Generated by Django 4.1.3 on 2023-04-20 19:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datascraper', '0002_rename_start_arch_date_archiverecord_arch_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='archiverecord',
            old_name='arch_date',
            new_name='arch_dt',
        ),
        migrations.RenameField(
            model_name='archiverecord',
            old_name='scrap_date',
            new_name='scrap_dt',
        ),
        migrations.RenameField(
            model_name='forecastsrecord',
            old_name='scrap_date',
            new_name='scrap_dt',
        ),
        migrations.RenameField(
            model_name='forecastsrecord',
            old_name='start_forec_date',
            new_name='start_forec_dt',
        ),
    ]
