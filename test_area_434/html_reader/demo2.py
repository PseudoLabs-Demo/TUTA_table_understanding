import requests
from bs4 import BeautifulSoup

URL = "https://pythonjobs.github.io/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
# print(soup)
# print(soup.prettify())
results = soup.find("section", {"class": "job_list"})
print(results.prettify())
# jobs = results.findAll("section")
# print(jobs)

# print(results)
