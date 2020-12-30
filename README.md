"picresize" は python によって jpg や png ファイルを指定されたサイズに変換します。
 
# DEMO
 
ブログにアップロードする写真や大きすぎる写真を一撃でリサイズしてくれます。
幅が足りない場合は希望のカラーで余白を埋めてくれます。（既定は黒になっています。）
 
![](https://tech-ojisan.com/wp-content/uploads/2020/12/image-18.png)
 
# 特徴
 
下記モジュールをインポートして使用していますので、 必要に応じて ` pip install ` を行ってください。

- os モジュール ファイルやフォルダを操作するモジュールです。
- Pillow は画像を簡易的に操作するライブラリです。 PIL という宣言で呼び出して、その中の Image というモジュールを使っています。 
```python
import os
from PIL import Image
```
処理中、実行ログも表示されるので便利です。
 
# 動作環境
 
* Python 3.8.7
* Pillow 8.0.1
 
# 使用方法
 
Pillow をインストールしてください。
 
```bash
pip install Pillow
```
 
img フォルダにリサイズしたいファイルをコピーして、picresize.py を実行してください。

## 設定
 
各パラメーターを操作して縦横操作可能。
縦長の写真については現在未対応。
![](https://tech-ojisan.com/wp-content/uploads/2020/12/image-20.png)