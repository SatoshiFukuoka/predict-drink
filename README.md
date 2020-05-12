# predict-drink
prediction of beer, coffee, or water

## 与えられた画像がビール、コーヒー、水を判定します。
Flaskを使用してWeb上で画像を読み込みます。

## 使い方
※以下のpre-trained　modelをダウンロードして'./'に置き、

1. download.py (引数:画像の種類）　Flickr APIを利用し、画像を収集

2. gen_data_augmented.py 画像を配列に入れ込む

3. drink_cnn_aug.py モデルの生成

4. predict.py 精度をチェック

5. predictflle.py web上で判定したい画像を受け取る(Flaskを使用）


