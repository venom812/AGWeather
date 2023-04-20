from django.http import HttpResponse
from django.templatetags.static import static

from django.conf import settings
from django.utils import timezone

from datetime import datetime
from .forecasts_scraper import scrap_forecasts
from .archive_scraper import scrap_archive_last_record
from .models import ForecastsRecord, ArchiveRecord

def ag_time(request):
    return HttpResponse(str(datetime.now()) + " | " + str(settings.USE_TZ) + " | " + str(timezone.now()))


def run_forecasts_scraper(request):

    json_forecasts_data = scrap_forecasts(static("datascraper_config.json"))
    local_datetime = datetime.now()
    local_datetime_iso = local_datetime.isoformat()

    try:
        record = ForecastsRecord.objects.get(rec_data=json_forecasts_data)
        return HttpResponse(local_datetime_iso + ' Record already exists: ' + str(json_forecasts_data[0]))
    
    except ForecastsRecord.DoesNotExist:
        record = ForecastsRecord(rec_date=local_datetime, rec_data=json_forecasts_data)
        record.save()
        return HttpResponse(local_datetime_iso + ' New record created: ' + str(json_forecasts_data[0]))

def run_archive_scraper(request):

    local_datetime = datetime.now()
    local_datetime_iso = local_datetime.isoformat()
    json_archive_data = scrap_archive_last_record(static("datascraper_config.json"))

    record, created = ArchiveRecord.objects.get_or_create(rec_data=json_archive_data,
                                                           defaults={'rec_date': local_datetime})
    if created:
        return HttpResponse(local_datetime_iso + ' New record created: ' + str(json_archive_data[0]))
    else:
        return HttpResponse(local_datetime_iso + ' Record already exists: ' + str(json_archive_data[0]))

