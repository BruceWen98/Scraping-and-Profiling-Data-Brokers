import requests
from bs4 import BeautifulSoup
import regexp_extractor as extract

USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"

def search(name):
  url = "https://www.google.com/search?q={}".format(name)
  resp = requests.get(url, headers = {"user-agent" : USER_AGENT})

  if resp.status_code == 200:
    page = resp.text
  else:
    return None

  soup = BeautifulSoup(page, features="lxml")
  # with open("output.html", "w") as file:
  #   file.write(str(soup))
  # print(soup)

  data={
    "from": "google.com",
    "url": url,
    "name": name,
    "results": []
  }

  for div in soup.select("div.rc"):
    a = div.select("a")[0]
    link=a["href"]
    title = a.select("h3")[0].text
    
    text = div.select("span.st")[0].text

    emails = extract.extract_email(text)
    # phones = extract.extract_phone(text)

    record = {
      "link": link,
      "title": title,
      "summary": text,
      "email": emails,
      # "phone": phones
    }
    data["results"].append(record)

  return data

