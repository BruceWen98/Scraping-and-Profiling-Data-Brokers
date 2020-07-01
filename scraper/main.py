import db
import scrape_google as google
import scrape_linkedin as linkedin
import scrape_peekyou as peekyou
import scrape_twitter_api as twitter
import scrape_thatsthem as thatsthem
import scrape_findpeoplesearch as findpeoplesearch
import scrape_facebook as facebook

import argparse

from dotenv import load_dotenv
load_dotenv()

parser = argparse.ArgumentParser(description="""
  search the data brokers
""")

parser.add_argument("first_name", help="First Name")
parser.add_argument("last_name", help="Last Name")

args = parser.parse_args()

first_name = args.first_name
last_name = args.last_name


def search_all(first_name, last_name):
  name = first_name + " " + last_name

  data = google.search(name)
  print(data)
  db.insert_or_update({ "name": name, "from": "google.com"}, data)

  data = linkedin.search(first_name, last_name)
  print(data)
  db.insert_or_update({ "name": name, "from": "linkedin.com"}, data)

  data = peekyou.search(first_name, last_name)
  print(data)
  db.insert_or_update({ "name": name, "from": "peekyou.com"}, data)

  data = twitter.search(name)
  print(data)
  db.insert_or_update({ "name": name, "from": "twitter.com"}, data)

  data = thatsthem.search(name)
  print(data)
  db.insert_or_update({ "name": name, "from": "thatsthem.com"}, data)

  data = findpeoplesearch.search(name)
  print(data)
  db.insert_or_update({ "name": name, "from": "findpeoplesearch.com"}, data)

  data = facebook.search(name)
  print(data)
  db.insert_or_update({ "name": name, "from": "facebook.com"}, data)

# people = [
#   # ("Raul", "Castro Fernandez"),
#   # ("Blase", "Ur"),
#   # ("Bruce", "Wen"),
#   # ("Timmy", "Lin")
# ]
# for (first_name, last_name) in people:
#   search_all(first_name, last_name)

print(first_name, last_name)
search_all(first_name, last_name)
