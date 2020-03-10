## 三重県内におけるコロナウイルス(Covid19)検査に関わる情報の収集

### 目的

三重県庁のページから，日別の検査数，陽性数，陰性数を取得し，機械可読なフォーマットとして出力しています．
ソースは下記のページを利用しています．

https://www.pref.mie.lg.jp/YAKUMUS/HP/m0068000071_00005.htm


### 使い方

```Shell
pip install -r requirements.txt
python3 main.py
```

data/にtsvファイルが作成されます．

### スケジュール

下記のbranchに3時間に1回の頻度で出力されます．

https://github.com/earlsuke/covid19-inspection-result-scraper-for-mie/tree/gh-pages

### 参考情報

- 三重県庁　新型コロナウイルス感染症について　https://www.pref.mie.lg.jp/YAKUMUS/HP/m0068000066.htm
- 東京都 新型コロナウイルス感染症対策サイト / Tokyo COVID-19 Task Force website https://github.com/tokyo-metropolitan-gov/covid19
- covid19hokkaido_scraping https://github.com/Kanahiro/covid19hokkaido_scraping
