import json
import requests
import datetime
from pprint import pprint
from bs4 import BeautifulSoup


def get_url(kategori):
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:58.0) Gecko/20100101 Firefox/58.0',
        'x-requested-with':
        'XMLHttpRequest'
    }

    date = datetime.date.today()
    stop = False
    result = []
    while not stop:
        url = 'http://www.tribunnews.com/index-news/{}?date={}'.format(
            kategori, date.strftime('%Y-%m-%d'))
        r = requests.get(url, headers=headers)
        print(date, url, len(result))
        if r.status_code != 200:
            date = date - datetime.timedelta(1)
        else:
            soup = BeautifulSoup(r.content, 'lxml')
            temp = soup.find('ul', {'class': 'lsi'}).findAll('h3')
            for i in temp:
                result.append({
                    'url': i.find('a')['href'],
                    'title': i.text.strip(),
                    'kategori': kategori
                })

            if len(result) < 500:
                date = date - datetime.timedelta(1)
            else:
                berenti = True
                break

    return result


if __name__ == '__main__':
    kategori = ['bisnis']
    for i in kategori:
        temp = get_url(i)
        with open('{}_url.json'.format(i), 'w') as output_file:
            json.dump(temp, output_file, indent=4)