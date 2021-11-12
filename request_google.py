from bs4 import BeautifulSoup
import requests, json, lxml

headers = {
    'User-agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582'
}

params = {
  'q': 'python',
  'gl': 'us',
  'hl': 'en',
}

#def get_searchquery_results():
html = requests.get('https://www.google.com/search', headers=headers, params=params).text
soup = BeautifulSoup(html, 'lxml')

data = []

print("\nTop 10 Results of Query: ")
for result in soup.select('.tF2Cxc'):
  title = result.select_one('.DKV0Md').text
  link = result.select_one('.yuRUbf a')['href']
  print(title, link, sep='\n')
  try:
    snippet = result.select_one('#rso .lyLwlc').text
  except: snippet = None

  data.append({
    'title': title,
    'link': link,
    'snippet': snippet,
  })

print("\nRelated searches: ")
for result in soup.select('.k8XOCe'):
    res = result.select_one('.s75CSd').text
    print(res)

for result in soup.select('.LHJvCe'):
    time = result.select_one('#result-stats').text
    print("\nSummary: " + time)
    # print("\nPeople also search for: ")
    # for result in soup.select('.exp-r'):
    #     search_for = result.select_one('.exp-r').text
    #     print(result)
#get_searchquery_results()
