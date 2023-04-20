"""Database models for Datscraper application."""
from django.db import models

class ForecastsRecord(models.Model):
    """Scraped forecasts data form sources in JSON format."""

    scrap_dt = models.DateTimeField()
    start_forec_dt = models.DateTimeField(db_index=True)
    forec_data_json = models.JSONField()
    
    def __str__(self):
        return self.start_forec_dt

class ArchiveRecord(models.Model):
    """Scraped weather archive data from source in JSON format."""

    scrap_dt = models.DateTimeField()
    arch_dt = models.DateTimeField(db_index=True)
    arch_data_json = models.JSONField()

    def __str__(self):
        return self.arch_dt
    
