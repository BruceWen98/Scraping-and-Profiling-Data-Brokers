import requests
import os
import time
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def create_driver(executable_path='driver/chromedriver'):
  options = webdriver.ChromeOptions()
  options.add_experimental_option("excludeSwitches", ["enable-automation"])
  options.add_experimental_option('useAutomationExtension', False)
  driver = webdriver.Chrome(options=options,executable_path=executable_path)

  driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": """
      Object.defineProperty(navigator, 'webdriver', {
        get: () => undefined
      })
    """
  })
  driver.execute_cdp_cmd("Network.enable", {})
  driver.execute_cdp_cmd("Network.setExtraHTTPHeaders", {"headers": {"User-Agent": "browser1"}})

  return driver

def search(name):
  driver = create_driver()
  data = search_by_name(driver, name)
  # driver.close()
  
  return data


def search_by_name(driver, name):
  # url = "https://www.whitepages.com/name/{}".format(name.replace(" ","_"))
  # url = "https://www.zabasearch.com/people/{}".format(name.replace(" ","+"))
  # url = "https://thatsthem.com"
  print(url)
  driver.get(url)

  # element = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.user_info > p.user_line1 > a")))
  #not enough, lets wait about 1min
  time.sleep(10)
  soup = BeautifulSoup(driver.page_source, features="lxml")

  with open("output.html", "w") as file:
    file.write(str(soup))
  print(soup)

  data={
    "from": "whitepages.com",
    "url": url,
    "name": name,
    "results": []
  }

  return data

if __name__ == "__main__":
  data = search("Raul Castro Fernandez")
  print(data)

