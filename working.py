from email import header
import requests
from bs4 import BeautifulSoup
import pandas as pd

def extract(page):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}
    url = f'https://in.indeed.com/jobs?q=software+developer+fresher&l=Kolkata&start=0'
    r = requests.get(url , headers)
    soup = BeautifulSoup(r.content , 'html.parser')
    return soup

def transform(soup):
    divs = soup.find_all('div' , class_ = 'cardOutline')
    for item in divs:
        title = item.find('h2' , class_ = 'jobTitle').text.strip()
        company = item.find('span' , class_ = 'companyName').text.strip()
        try:
            salary = item.find('div' , class_ = 'attribute_snippet').text.strip()
        except:
            salary = ''
        summary = item.find('div' , class_ = 'job-snippet').text.strip().replace('\n','')


        job = {
            'title' : title,
            'company' : company,
            'salary' : salary,
            'summary' : summary
        }      
        joblist.append(job)
    return    


joblist = []

for i in range(0 , 40 , 10):
    print(f'Getting page, {i}')
    c = extract(0)    
    transform(c)

df = pd.DataFrame(joblist) 

print(df.head() )
df.to_csv('jobs.csv')




