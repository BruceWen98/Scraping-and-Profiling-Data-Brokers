import requests
import os
import time
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def create_driver(executable_path='driver/chromedriver'):
  driver = webdriver.Chrome(executable_path)
  return driver

def search(first_name, last_name):
  driver = create_driver()
  data = search_by_name(driver,first_name, last_name)
  # driver.close()
  
  return data

def search_by_name(driver, first_name, last_name):
  url = "https://www.peekyou.com/{}_{}".format(first_name, last_name)
  print(url)
  driver.get(url)

  # element = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.user_info > p.user_line1 > a")))
  #not enough, lets wait about 1min
  time.sleep(10)
  soup = BeautifulSoup(driver.page_source, features="lxml")
  
  with open("output.html", "w") as file:
    file.write(str(soup))

  results=[]
  for div in soup.select("div#liveWebResults div"):
    next_div = div.find_next_sibling()
    if next_div:
      h3 = next_div.select_one("h3")
      if h3 and h3.text == "Arrest Records & Driving Infractions":
        print("Ignore the section of useless data...")
        break

    for user_info in div.select("div.user_info"):
      title = user_info.select_one("p.user_line1 a")
      title_text = title.get_text(strip=True)# the name of the people
      # print(title_text)

      exist = False
      for r in results:
        if r["name"] == title_text:
          exist=True
          break

      if exist: #already saved, ignore
        continue

      record={
        "name": title_text,
      }
         
      for index, span in enumerate(user_info.select("p.user_line3 span")):
        record["line{}".format(index + 1)]  = span.text

      results.append(record)

  data={
    "from": "peekyou.com",
    "url": url,
    "name": "{} {}".format(first_name, last_name),
    "results": results,
  }
  return data

if __name__ == "__main__":
  data = search("Raul", "Castro Fernandez")
  print(data)