# !/usr/bin/env python3

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

from persistence import save
from time_conversion import convert_post_date_to_sortable_format, convert_end_date_to_sortable_format


URL = 'https://www.cv.ee/toopakkumised/infotehnoloogia?sort=inserted&dir=desc'
soup = BeautifulSoup(urlopen(URL), 'html.parser')

found_adverts = []

for advert in soup.findAll('div', {'itemtype': 'http://schema.org/JobPosting'}):
  if('offer_company_premium' in advert['class']):
    # Ignore extra premium offers
    continue
  if('cvo_premium_offer' in advert['class']):
    # Ignore premium offers
    continue

  title_block = advert.find('a', {'onclick': 'Cvo.jobs.saveSearch();'})
  job_title = title_block.text
  url = 'http:' + title_block['href']

  img_tag = advert.find('img')
  if img_tag != None:
    logo_url = 'http:' + img_tag['src']
  else:
    logo_url = ''

  company = advert.find('li', {'class': 'offer-company'}).text
  location = advert.find('li', {'class': 'offer-location'}).text

  dates_block = advert.find('ul', {'class': 'cvo_module_offer_meta offer_dates'})
  post_date = re.search('\d+\. [a-zA-Z]+ \d\d\d\d \d\d:\d\d', str(dates_block)).group()
  end_date = re.search('\d\d.\d\d.\d\d\d\d', dates_block.text).group()

  post_date = convert_post_date_to_sortable_format(post_date)
  end_date = convert_end_date_to_sortable_format(end_date)

  found_adverts += [(company, job_title, location, url, logo_url, post_date, end_date)]


save(found_adverts)