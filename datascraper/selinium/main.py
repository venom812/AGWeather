# import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import time



def get_source_html(url):

    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_argument("--disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(
        executable_path="/home/anton/agweather/AGWeather/datascraper/selinium/chromedriver",
        # options=options
    )

    driver.maximize_window()


    try:
        driver.get(url=url)

        time.sleep(10)

        # driver.get("https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html")
        print(driver.page_source)
    except Exception as _ex:
        print(_ex)
    finally:
        driver.close()
        driver.quit()


def main():
    url = "https://rp5.ru/%D0%9F%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0_%D0%B2_%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3%D0%B5"
    
    get_source_html(url)



if __name__ == "__main__":
    main()
