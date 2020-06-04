import requests
from bs4 import BeautifulSoup
url = "https://www.monster.com/jobs/search/?q=Software-Developer&where=Australia"
r = requests.get(url)
htmlContent= r.content
soup=BeautifulSoup(htmlContent,'html.parser')
#print(soup.prettify())
results = soup.find(id='ResultsContainer')
#print(results.prettify())
job_elems = results.find_all('section', class_='card-content')
for job_elem in job_elems:
    print(job_elem, end='\n'*2)
for job_elem in job_elems:
    # Each job_elem is a new BeautifulSoup object.
    # You can use the same methods on it as you did before.
    title_elem = job_elem.find('h2', class_='title')
    company_elem = job_elem.find('div', class_='company')
    location_elem = job_elem.find('div', class_='location')
    print(title_elem)
    print(company_elem)
    print(location_elem)
    print() 