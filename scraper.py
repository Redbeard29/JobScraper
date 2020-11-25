import requests
from bs4 import BeautifulSoup

URL = 'https://www.monster.com/jobs/search/?q=Software-Developer&where=Pittsburgh__2C-PA'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(id='ResultsContainer')

job_elements = results.find_all('section', class_='card-content')


for job in job_elements:
    job_title = job.find('h2', class_="title")
    job_company= job.find('div', class_="company")
    job_location = job.find('div', class_="location")
    if None in (job_title, job_company, job_location):
        continue
    if 'Sr' in (job_title.text):
        continue
    if 'Senior' in (job_title.text):
        continue
    if 'Principal' in (job_title.text):
        continue

    print(job_title.text.strip())
    print(job_company.text.strip())
    print(job_location.text.strip())
    print()

