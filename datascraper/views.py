from django.http import HttpResponse
from django.templatetags.static import static

from django.conf import settings
from django.utils import timezone

from datetime import datetime
from .forecasts_scraper import scrap_forecasts
from .archive_scraper import scrap_archive_last_record
from .models import ForecastsRecord, ArchiveRecord, DatascraperLog


def run_forecasts_scraper(request):

    start_forec_date, forec_data_json = scrap_forecasts(static("datascraper_config.json"))

    dt = datetime.now()
    dt_iso = dt.isoformat()
    msg = dt_iso

    try:
        record = ForecastsRecord.objects.get(start_forec_dt=start_forec_date)

        if str(record.forec_data_json) != str(forec_data_json).replace(')',']').replace('(','['):
            print(type(record.forec_data_json),type(forec_data_json))
            record.forec_data_json, record.scrap_dt = forec_data_json, dt
            record.save()

            msg += ' Forec Record updated'
        else:
            msg += ' Forec Record already exists'
    
    except ForecastsRecord.DoesNotExist:
        record = ForecastsRecord(scrap_dt=datetime.now(), 
                                 start_forec_dt=start_forec_date, 
                                 forec_data_json=forec_data_json)
        record.save()

        msg += ' New Forec record created'

    finally:
        DatascraperLog.objects.create(log_dt=dt,log_str=msg)
        return HttpResponse(msg)

def run_archive_scraper(request):

    arch_datetime, arch_data_json = scrap_archive_last_record(static("datascraper_config.json"))

    dt = datetime.now()
    dt_iso = dt.isoformat()
    msg = dt_iso

    record, created = ArchiveRecord.objects.get_or_create(arch_dt = arch_datetime,
                                                          arch_data_json = arch_data_json,
                                                          defaults={'scrap_dt': dt})
    
    msg += ' New Arch record created' if created else ' Arch Record already exists'
    DatascraperLog.objects.create(log_dt=dt,log_str=msg)
    return HttpResponse(msg)


def ag_time(request):
    return HttpResponse(str(datetime.now()) + " | " + str(settings.USE_TZ) + " | " + str(timezone.now()))