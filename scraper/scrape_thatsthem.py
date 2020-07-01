import requests
import os
import time
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
    driver = webdriver.Chrome(executable_path)
  return driver

def search(name):
  driver = create_driver()
  data = search_by_name(driver, name)
  # driver.close()
  
  return data


def search_by_name(driver, name_to_search):
  url = "https://thatsthem.com/name/{}".format(name_to_search.replace(" ","-"))
  print(url)
  driver.get(url)

  soup = BeautifulSoup(driver.page_source, features="lxml")

  # with open("output.html", "w") as file:
  #   file.write(str(soup))
  # print(soup)
  results = []
  for div in soup.select("div.ThatsThem-record"):
    record = {}
    overview = div.select_one("div.ThatsThem-record-overview")
    name = overview.select_one("h2 span").get_text()
    record["name"] = name

    addrs = []
    addr_spans = overview.select("div.ThatsThem-record-address span span")
    for s in addr_spans:
      addrs.append(s.text)
    if addrs:
      record["address"]=" ".join(addrs)
    
    meta = div.select_one("div.ThatsThem-record-meta")
    age = meta.select_one("div.ThatsThem-record-age span.active")
    if age:
      record["age"] = age.get_text(strip=True)

    details = div.select_one("div.ThatsThem-record-details")
    record["details"] = {}
    for tab in details.select("dl.row"):
      keys = []
      for dt in tab.select("dt"):
        keys.append(dt.text)
      values=[]
      for dd in tab.select("dd"):
        values.append(dd.get_text(strip=True))
      
      dict_raw = dict(zip(keys, values))
      dict_cleaned = dict((k, v) for k, v in dict_raw.items() if v)
      record["details"].update(dict_cleaned)
    results.append(record)

  data={
    "from": "thatsthem.com",
    "url": url,
    "name": name_to_search,
    "results": results,
  }

  return data

if __name__ == "__main__":
  data = search("Blase Ur")
  print(data)
  # time.sleep(3600)

