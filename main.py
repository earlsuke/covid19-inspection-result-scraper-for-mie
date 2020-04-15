import lxml.html
import requests
from codecs import open
from mojimoji import zen_to_han
import re

URL = 'https://www.pref.mie.lg.jp/YAKUMUS/HP/m0068000071_00005.htm'
HIHOKEN_NUM_PAT = re.compile('\(([\d]+)\)')

def clean_string(x: str) -> str:
    return x.replace('月','/').replace(' ','').replace('日', '').replace('\u3000', '').replace('件', '').replace('\r','').replace('\n','').replace('\t','')


def main():

    resp = requests.get(URL, timeout=(3.0, 7.5))
    resp.encoding = resp.apparent_encoding

    if resp.status_code != 200:
        # failed to load
        raise ValueError('Failed to load the target web page : {}'.format(URL))

    # parse html into an element
    root = lxml.html.fromstring(resp.text)
    items = root.find_class("main-text")[0].findall("div/table/tbody/tr")

    with open('data/data.tsv', 'w') as wb:
        N = len(items)
        for num, i in enumerate(items):
            if any([x.text_content() == None for x in i.getchildren()]):
                continue

            if num == N-1:
                break

            if num == 0:
                data = [x.text.replace(' ','').replace('\u3000', '') for x in i.getchildren()]
            else:
                # date, hihokensya, inspections, positive cases, negative cases
                data = []

                for ix, tr in enumerate(i.getchildren()):

                    text = zen_to_han(clean_string(str(tr.text_content())))

                    if ix == 1:
                        pmatch = HIHOKEN_NUM_PAT.search(text)

                        if pmatch:
                            res = str(pmatch.groups()[0])
                            text = text.replace('('+res+')', '')

                        else:
                            res = "0"
                        
                        data.append(text)
                        data.append(res)
                    else:
                        data.append(text)
                    
                wb.write('\t'.join(data) + '\n')
    

if __name__ == '__main__':
    main()
