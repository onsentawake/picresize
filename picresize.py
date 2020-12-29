
'''
jpg のサイズを一括リサイズ。
同一階層に [img] [resize] それぞれのフォルダを作成します。
[img] ファイルに元画像 [resize] フォルダにリサイズ後の画像を吐き出します。
pip で pillow をインストールします。

※Py3.9入れたらPILのインポートができない。　3.8に戻したら今度はimgパスが見つからない。
jupyter lab ではうまくいく。FileNotFoundError: [WinError 3] 指定されたパスが見つかりません。: 'img'
'''
# os モジュールは ファイルやフォルダを操作する際に必要になるモジュール。
# Pillow は画像を簡易的に操作するライブラリ。PIL という宣言で呼び出して、その中の Image というモジュールを使う。
import os
from PIL import Image

# 名前の通りimg resize それぞれを変数に代入。
dir_name = 'img'
new_dir_name = 'resize'

# os.dir()で引数のディレクトリの中身をリストで表示してくれる。
files = os.listdir(dir_name)

# img から resize に変換した画像を書き込みます。
for file in files: # リストの途中から記述したいときの書き方を忘れていた。[1:5]で1~5の画像を取得という書き方もできる。
    img = Image.open(os.path.join(dir_name,file)) # openはそのままの意味。path.join()で引数を結合してpathにしてくれる。dir_nameフォルダからオープン。
    img_resize = img.resize((600,337)) # 今回はサイズ指定。アスペクト比固定でリサイズするのが目標。
    
    img_resize.save(os.path.join(new_dir_name,file)) # 変数を引数のpathに保存。今回はnew_dir_name に保存。



