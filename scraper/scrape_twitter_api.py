import requests
import os
import time
from dotenv import load_dotenv
load_dotenv()

TWITTER_API_KEY=os.getenv("TWITTER_API_KEY")
TWITTER_API_KEY_SECRET=os.getenv("TWITTER_API_KEY_SECRET")
TWITTER_TOKEN=os.getenv("TWITTER_TOKEN")
TWITTER_TOKEN_SECRET=os.getenv("TWITTER_TOKEN_SECRET")

from twitter import *


def search(name):
  api = Twitter(auth=OAuth(TWITTER_TOKEN, TWITTER_TOKEN_SECRET, TWITTER_API_KEY, TWITTER_API_KEY_SECRET))
  users = api.users.search(q=name)

  data={
    "from": "twitter.com",
    "url": "twitter api",
    "name": name,
    "results": []
  }

  keys = []
  for key in """
    name
    screen_name
    location
    url
    description
    profile_image_url_https
  """.splitlines():
    key=key.strip()
    if key != "":
      keys.append(key)

  print(keys)

  for user in users:
    record={}
    for key in keys:
      record[key]=user[key]
    
    if "status" in user.keys() and user["status"]:
      record["latest_twitter"]=user["status"]["text"]
      record["latest_twitter_at"]=user["status"]["created_at"]
    data["results"].append(record)
  return data

if __name__ == "__main__":
  data = search("Raul Castro Fernandez")
  print(data)


