import lxml.html
import requests
from codecs import open
from mojimoji import zen_to_han

URL = 'https://www.pref.mie.lg.jp/YAKUMUS/HP/m0068000071_00005.htm'

def main():

    resp = requests.get(URL)
    resp.encoding = resp.apparent_encoding

    if resp.status_code != 200:
        # failed to load
        raise ValueError('Failed to load the target web page : {}'.format(URL))

    # parse html into an element
    root = lxml.html.fromstring(resp.text)
    items = root.xpath("//*[@id='section1']/div/div/div[1]//tr")

    with open('data/data.tsv', 'w') as wb:
        N = len(items)
        for num, i in enumerate(items):
            if num == N-1:
                break

            if num == 0:
                data = [x.text.replace(' ','').replace('\u3000', '') for x in i.getchildren()]
            else:
                # date, inspections, positive cases, negative cases
                data = [zen_to_han(x.text).replace('月','/').replace(' ','').replace('日', '').replace('\u3000', '').replace('件', '') for x in i.getchildren()]

            wb.write('\t'.join(data) + '\n')
    

if __name__ == '__main__':
    main()