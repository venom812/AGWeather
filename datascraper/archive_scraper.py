"""Module scrapes data from archive source."""
from datetime import datetime
from json import load
import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    from forecasts_scraper import month_rusname_to_number, scraper_error
else:
    from .forecasts_scraper import month_rusname_to_number, scraper_error


def scrap_archive_last_record(path_to_config_file):
    """Run scarping last archive record process."""
    # Reading configuration file
    with open(path_to_config_file, 'r', encoding='UTF-8') as file:
        datascraper_config = load(file)
    source_config = datascraper_config["archive_source"]

    try:
        req = requests.post(source_config['url'],
                            cookies=source_config['cookies'],
                            headers=source_config['headers'],
                            proxies=datascraper_config['proxies'],
                            timeout=10)
        src = req.text
        soup = BeautifulSoup(src, "lxml")

        # Parsing archive table data
        arch_row = soup.find('table', id='archiveTable').find_all('tr')[1]

        # Parsing source datetime
        date_time = arch_row.find('td', class_='cl_dt').get_text()
        date_time = [date_time[:4],*date_time.split('г.')[-1].split(',')[0].split('\xa0')[::-1]]
        date_time[1] = str(month_rusname_to_number(date_time[1])).zfill(2)
        date_time = '-'.join(date_time) + 'T' + \
                   arch_row.find_all('td')[-29].get_text() + ":00:00"
        date_time = datetime.fromisoformat(date_time)

        # Parsing  temp, pressure, wind_speed
        arch_row = arch_row.find_all('td')
        temp = float(arch_row[-28].div.get_text())
        press = float(arch_row[-27].div.get_text())
        wind = arch_row[-22]
        wind = int(wind.div.get_text().strip().split(' ')[0][1:]) if wind.div else 0

        return  date_time, (temp, press, wind)

    except AttributeError:
        scraper_error(source_config['name'])
        return


if __name__ == '__main__':

    arc = scrap_archive_last_record("static/datascraper_config.json")
    print(arc)
