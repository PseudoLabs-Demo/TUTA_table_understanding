import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="ResultsContainer")
job_elements = results.find_all("div", class_="card-content")

python_jobs = results.find_all(
    "h2", string=lambda text: "python" in text.lower())

python_jobs_elements = [
    h2_element.parent.parent.parent for h2_element in python_jobs]

# for job_element in job_elements:
#     title_element = job_element.find("h2", class_="title").text.strip()
#     subtitle_element = job_element.find("h3", class_="company").text.strip()
#     location_element = job_element.find("p", class_="location").text.strip()

#     print(title_element)
#     print(subtitle_element)
#     print(location_element)

#     print()
#     break

for job_element in python_jobs_elements:

    title_element = job_element.find("h2", class_="title").text.strip()
    subtitle_element = job_element.find("h3", class_="company").text.strip()
    location_element = job_element.find("p", class_="location").text.strip()

    links = job_element.find_all("a")
    second_link_url = links[1]["href"]
    print(f"Link {second_link_url}")
    # for link in links:
    #     # print(link.text.strip())
    #     link_url = link["href"]
    #     print(f"Link {link_url}")
    # print("links")
    # print(links)

    print(title_element)
    print(subtitle_element)
    print(location_element)

    print()


# print(results.prettify())
