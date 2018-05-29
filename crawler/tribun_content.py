import re
import json
import time
import requests
from pprint import pprint
from tqdm import tqdm
from bs4 import BeautifulSoup


def get_content(url):
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:58.0) Gecko/20100101 Firefox/58.0',
        'x-requested-with':
        'XMLHttpRequest'
    }

    r = requests.get(url, headers=headers)
    url = r.url
    if r.status_code != 200:
        return False
    else:
        soup = BeautifulSoup(r.content, 'lxml')
        result = {
            'title':
            soup.find('h1').text,
            'content':
            '\n'.join([
                i.text for i in soup.find('div', {
                    'class': 'side-article txt-article'
                }).findAll('p')
            ])
        }
        result['content'] = re.sub(r'\s+', ' ', result['content']).strip()
        return result


if __name__ == '__main__':
    kategori = ['bisnis', 'sains', 'sport']
    for kat in kategori:
        result = []
        with open('{}_url.json'.format(kat), 'r') as output_file:
            data = json.loads(output_file.read())

        for i in tqdm(data):
            try:
                temp = get_content(i['url'])
                temp['kategori'] = i['kategori']
                result.append(temp)
            except Exception:
                continue

        with open('{}_content.json'.format(kat), 'w') as output_file:
            json.dump(result, output_file, indent=4)
