import urllib3 as url3
from bs4 import BeautifulSoup as bs

url="yahooweatherの調べた地域のurl"

#urlにアクセスし、戻り値には結果やhtml
url_3=url3.PoolManager()
instance=url_3.request("GET",url)
#instanceという名の変数からhtmlを取り出し、bs(BeautifulSoup)で使えるようにバース（プログラムで扱えるようにする処理）する
soup=bs(instance.date,"html.parser")

#今日の天気を取得する
today_weather=soup.select_one("#main>div.forecastCity>table>tr>td>dv>p.pict")
print("today's weather is:"+today_weather)

#明日の天気を取得する
tomorrow_weather=soup.select_one("#main>div.forecastCity>table>tr>td>dv>p.pict")
print("tomorrow's weather is:"+tomorrow_weather)

#すぐ消える対策として、入力されるまで待機
input()