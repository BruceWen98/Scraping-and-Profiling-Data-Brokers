import requests
import os
import time
import re
from dotenv import load_dotenv
load_dotenv()

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
  driver.get("https://facebook.com")
  driver.find_element_by_id("email").send_keys(os.getenv("FACEBOOK_USER"))
  driver.find_element_by_id("pass").send_keys(os.getenv("FACEBOOK_PASS"))
  
  driver.find_element_by_xpath("//input[@value='Log In']").click()
  element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@name='q']")))

  #then we search by people
  url = "https://www.facebook.com/search/people/?q={}".format(name)
  driver.get(url)

  soup = BeautifulSoup(driver.page_source, features="lxml")

  # with open("output.html", "w") as file:
  #   file.write(str(soup))
  # print(soup)

  results = []
  for i, div in enumerate(soup.select("div#BrowseResultsContainer div.clearfix")):
    hash={}
    if i > 10:
      break #stop at 10 results

    img=div.select_one("img.img")
    if img:
      hash["avatar"]=img["src"]
    
    span = div.select_one("div > a > span")
    if span:
      hash["name"] = span.text
      hash["link"] = span.parent["href"]  
    results.append(hash)

  data={
    "from": "facebook.com",
    "url": url,
    "name": name,
    "results": results,
  }

  return data

if __name__ == "__main__":
  data = search("Blase Ur")
  print(data)
  # time.sleep(120)

