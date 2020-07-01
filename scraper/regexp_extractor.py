import re

def extract_email(text):
  return re.findall('[a-zA-Z0-9_\-\.]+@[a-zA-Z0-9_\-\.]+\.[a-zA-Z]{2,5}', text)

def extract_phone(text):
  return re.findall('\(?\+?[0-9]*\)?[0-9_\- \(\)]*', text)