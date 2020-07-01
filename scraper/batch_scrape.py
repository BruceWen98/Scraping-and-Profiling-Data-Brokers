import db
import scrape_google as google
import scrape_linkedin as linkedin
import scrape_peekyou as peekyou
import scrape_twitter_api as twitter
import scrape_thatsthem as thatsthem
import scrape_findpeoplesearch as findpeoplesearch
import scrape_facebook as facebook

from dotenv import load_dotenv
load_dotenv()

def search_all(first_name, last_name):
  name = first_name + " " + last_name

  # data = google.search(name)
  # print(data)
  # db.insert_or_update({ "name": name, "from": "google.com"}, data)

  # data = linkedin.search(first_name, last_name)
  # print(data)
  # db.insert_or_update({ "name": name, "from": "linkedin.com"}, data)

  # data = peekyou.search(first_name, last_name)
  # print(data)
  # db.insert_or_update({ "name": name, "from": "peekyou.com"}, data)

  # data = twitter.search(name)
  # print(data)
  # db.insert_or_update({ "name": name, "from": "twitter.com"}, data)

  data = thatsthem.search(name)
  print(data)
  db.insert_or_update({ "name": name, "from": "thatsthem.com"}, data)

  # data = findpeoplesearch.search(name)
  # print(data)
  # db.insert_or_update({ "name": name, "from": "findpeoplesearch.com"}, data)

  # data = facebook.search(name)
  # print(data)
  # db.insert_or_update({ "name": name, "from": "facebook.com"}, data)

people = [
  # ("Raul", "Castro Fernandez"),
  # ("Blase", "Ur"),
  # ("Bruce", "Wen"),
  # ("Timmy", "Lin"),

  # ("Vincent",  "Pan"),
  # ("Kevin",  "Wu"),
  # ("Simon",  "Zhang"),
  # ("Lynnette",  "Jiang"),
  # ("Barbara",  "Schubert"),
  # ("Patrick",  "Napouk"),
  # ("Steve",  "Marcus"),
  # ("Galen",  "Harrison"),

  #That's them daily quota exceeds. 8 per day?
  ("Alexandra",  "Nisenoff"),
  ("Graham",  "Middleton"),
  ("Colin",  "Rydell"),
  ("Audrey",  "Morrison")
]

for (first_name, last_name) in people:
  search_all(first_name, last_name)


