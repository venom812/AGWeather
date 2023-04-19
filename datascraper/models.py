"""Database models for Datscraper application."""
from django.db import models

class ForecastsRecord(models.Model):
    """Scraped forecasts data form sources in JSON format."""

    rec_date = models.DateTimeField()
    rec_data = models.JSONField()
    
    def __str__(self):
        return self.rec_date
    
    class Meta:
        ordering = ["rec_date"]

class ArchiveRecord(models.Model):
    """Scraped weather archive data from source in JSON format."""

    rec_date = models.DateTimeField()
    rec_data = models.JSONField()

    def __str__(self):
        return self.rec_date
    
    class Meta:
        ordering = ["rec_date"]