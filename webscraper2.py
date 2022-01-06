from bs4 import BeautifulSoup as soup
import requests
import csv

source = requests.get('https://coreyms.com/').text

soup = soup(source, 'lxml')

csv_file = open('cms_scrape.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline','summary','link'])

articles = soup.find_all('article')

for article in articles:

    headline = article.h2.a.text
    print(headline)

    summary = article.find('div', class_='entry-content').p.text
    #print(summary)

    try:
        videoSource = article.find('iframe', class_='youtube-player')['src'].split('/')[4].split('?')[0]
        yt_link = f'https://youtube.com/watch?v={videoSource}'

    except Exception as e:
        yt_link = None

    print(yt_link)
    print()

    csv_writer.writerow([headline, summary,yt_link])

csv_file.close()