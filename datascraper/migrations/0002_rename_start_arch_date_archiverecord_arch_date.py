# Generated by Django 4.1.3 on 2023-04-20 19:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datascraper', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='archiverecord',
            old_name='start_arch_date',
            new_name='arch_date',
        ),
    ]