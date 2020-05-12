# predict-drink
prediction of beer, coffee, or water

## 与えられた画像がビール、コーヒー、水かを判定します。
Flaskを使用してWeb上で画像を読み込みます。

## 使い方
※以下のファイルの中身を'./'に置き、

https://d.kuku.lu/3174a794e

set FLASK_APP=predictfile.py

python -m flask run --host=0.0.0.0 --port=8080 --without-threads

とすれば利用できます。

以下各モジュールの簡易説明

1. download.py (引数:画像の種類）　Flickr APIを利用し、画像を収集

2. gen_data_augmented.py 画像を配列に入れ込む

3. drink_cnn_aug.py モデルの生成

4. predict.py 精度をチェック

5. predictflle.py web上で判定したい画像を受け取る(Flaskを使用）

## 参考にしたもの
【画像判定AIアプリ開発・パート1】TensorFlow・Python・Flaskで作る画像判定AIアプリ開発入門
https://www.udemy.com/course/tensorflow-advanced/
