import requests
import os
import time
import re

from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def create_driver(executable_path='driver/chromedriver', proxy=None):
  if proxy:
    options = webdriver.ChromeOptions()
    options.add_argument('--proxy-server=%s' % proxy )
    driver = webdriver.Chrome(options=options,executable_path=executable_path)
  else:
    driver = webdriver.Chrome(executable_path=executable_path)
  return driver

def search(name):
  driver = create_driver()
  data = search_by_name(driver, name)
  # driver.close()
  
  return data


def search_by_name(driver, name):
  url = "https://findpeoplesearch.com"
  print(url)
  
  results = []
  data={
    "from": "findpeoplesearch.com",
    "url": url,
    "name": name,
    "results": results,
  }

  driver.get(url)
  
  driver.find_element_by_id("full_name").send_keys(name);
  driver.find_element_by_id("button-search").click()
  
  try:
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "new-search")))
    soup = BeautifulSoup(driver.page_source, features="lxml")
  except:
    return data

  # with open("output.html", "w") as file:
  #   file.write(str(soup))
  # print(soup)


  for panel in soup.select("div.row div.panel"):
    record = {}
    heading = panel.select_one("div.panel-heading")
    found_name = heading.select_one("span.head_name").get_text(strip=True)
    record["name"] = found_name.replace(u'\xa0', ' ')

    hash = {}
    body = panel.select_one("div.panel-body")
    for col in body.select("div"):
      elem_key = col.select_one("span.data_header")
      if not elem_key:
        continue

      key = elem_key.get_text(strip=True)
      values=[]
      for link in col.select("h6 a"):
        val = link.get_text(strip=True)
        if re.search("view more", val, re.IGNORECASE):
          continue
        values.append(val)
      if values:
        hash[key] = values
    record["details"] = hash
    results.append(record)



  return data

if __name__ == "__main__":
  data = search("Blase Ur")
  print(data)
  time.sleep(120)


