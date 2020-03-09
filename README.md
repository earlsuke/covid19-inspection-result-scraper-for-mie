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

### 参考情報

https://www.pref.mie.lg.jp/YAKUMUS/HP/m0068000066.htm
