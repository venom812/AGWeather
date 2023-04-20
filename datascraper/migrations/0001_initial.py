# Generated by Django 4.1.3 on 2023-04-20 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArchiveRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scrap_date', models.DateTimeField()),
                ('start_arch_date', models.DateTimeField(db_index=True)),
                ('arch_data_json', models.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='ForecastsRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scrap_date', models.DateTimeField()),
                ('start_forec_date', models.DateTimeField(db_index=True)),
                ('forec_data_json', models.JSONField()),
            ],
        ),
    ]
