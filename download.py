from flickrapi import FlickrAPI
from urllib.request import urlretrieve
from pprint import pprint
import os,time,sys

#APIキーの情報

key = "d1732328002188f9fe5c59f497299d79"
secret = "13163d1250ca1eda"
wait_time = 1

#保存フォルダの指定
drinkname = sys.argv[1]
savedir = "./" + drinkname

flickr = FlickrAPI(key, secret, format='parsed-json')
result = flickr.photos.search(
        text = drinkname,
        per_page = 400,
        media = 'photos',
        sort = 'relevance', #関連順に並べる
        safe_search = 1,
        extras = 'url_q, licence'#出力情報　画像データ　ライセンス
)

photos = result['photos']
#返値を表示


for i,photo in enumerate(photos['photo']):
    url_q = photo['url_q']
    filepath = savedir + '/' + photo['id'] + '.jpg'
    if os.path.exists(filepath): continue
    urlretrieve(url_q,filepath)
    time.sleep(wait_time)
