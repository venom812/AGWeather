from django.urls import path

from . import views

urlpatterns = [
    path('run_forecasts_scraper', views.run_forecasts_scraper, name='run_forecasts_scraper'),
    path('run_archive_scraper', views.run_archive_scraper, name='run_archive_scraper'),
]