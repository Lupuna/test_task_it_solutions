from selenium import webdriver
import undetected_chromedriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from time import sleep
from random import randrange, choice
from selenium.webdriver.common.by import By


def simulate_user(url: str):
    options = webdriver.ChromeOptions()
    user_agents = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, как Gecko) Chrome/110.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, как Gecko) Chrome/111.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, как Gecko) Chrome/112.0.0.0 Safari/537.36'
    ]
    options.add_argument(f'user-agent={choice(user_agents)}')
    # options.add_argument('--headless')
    options.add_argument('--disable-blink-features=AutomationControlled')
    driver = undetected_chromedriver.Chrome(options=options)
    try:
        driver.get(url)
        sleep(5)
        items = driver.find_elements(By.XPATH, "//div[@class='bull-item__subject-container']/a")[0:10]
        for item in items:
            item.send_keys(Keys.CONTROL + Keys.RETURN)
            sleep(randrange(1, 3))
            driver.switch_to.window(driver.window_handles[-1])
            print(driver.page_source)
            sleep(randrange(2, 3))
            driver.close()
            driver.switch_to.window(driver.window_handles[0])

    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()


if __name__ == '__main__':
    simulate_user('https://www.farpost.ru/vladivostok/service/construction/guard/+/Системы+видеонаблюдения/')
