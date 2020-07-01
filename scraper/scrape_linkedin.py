import requests
import os
from bs4 import BeautifulSoup
import regexp_extractor as extract

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def search(first_name, last_name):
  driver = create_driver()
  login(driver)
  data = search_by_name(driver,first_name, last_name)
  driver.close()
  
  return data

def create_driver(executable_path='driver/chromedriver'):
  driver = webdriver.Chrome(executable_path)
  return driver

def login(driver):
  email = os.getenv("LINKEDIN_USER")
  password = os.getenv("LINKEDIN_PASS")

  driver.get("https://www.linkedin.com/login")
  element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username")))

  email_elem = driver.find_element_by_id("username")
  email_elem.send_keys(email)

  password_elem = driver.find_element_by_id("password")
  password_elem.send_keys(password)
  driver.find_element_by_tag_name("button").click()

  element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "profile-nav-item")))


def search_by_name(driver, first_name, last_name):
  url = "https://www.linkedin.com/pub/dir?firstName={}&lastName={}".format(first_name, last_name)
  print(url)
  driver.get(url)
  
  soup = BeautifulSoup(driver.page_source, features="lxml")
  # with open("output.html", "w") as file:
  #   file.write(str(soup))

  results=[]
  for div in soup.select("div.search-result__wrapper"):
    #the image part
    image = div.select_one("div.search-result__image-wrapper")
    img = image.select_one("img")
    #some have no image
    img_src = None
    if img:
      img_src = img.attrs["src"]
    

    #the info part:
    info = div.select_one("div.search-result__info")
    link = info.select_one("a").attrs["href"]
    name = info.select_one("span.name").text
  
    line1 = info.select_one("p.subline-level-1").get_text(strip=True)
    line2 = info.select_one("p.subline-level-2").get_text(strip=True)
    results.append({
      "link": link,
      "title": name,
      "line1": line1,
      "line2": line2,
      "img": img_src,
    })

  data={
    "from": "linkedin.com",
    "url": url,
    "name": "{} {}".format(first_name, last_name),
    "results": results,
  }

  return data
