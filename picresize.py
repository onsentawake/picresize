
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

def generate_thumbnail_360x195(origin_path, dest_path, quality=70): # 完成するファイルのパス
    """Resize image to 360x195.
    As horizontal direction precedes, vertical direction is possible to get white spaces.
    画像のリサイズするよ！"""

    pil_origin = Image.open(origin_path)
    print(f'{origin_path} Original size is... {pil_origin.size}')
    w, h = pil_origin.size # オリジナルの画像サイズをw,hに入れます。

    # Width 360px
    resize_rate = 500/w
    pil_w360 = pil_origin.resize((int(w*resize_rate), int(h*resize_rate)))
    w, h = pil_w360.size # 縦、横の長さを入れる。（.sizeでタプルで写真のサイズを返してくれる）

    # 360x195の写真を生成。引数の0,0,0,は、縦が足りなかったときに補完する色。この場合は横長な写真だった場合黒色で縦を埋める。
    bg = Image.new('RGB', [360, 195], (0, 0, 0)) # 新しく生成する画像のサイズ。
    bg.paste(pil_w360, (0, int((195-h)/2))) # 縦のサイズが足りない場合、上下に bg 変数で指定した色で背景を追加。
    bg.save(dest_path, quality=quality)

# img から resize に変換した画像を書き込みます。
for file in files: # リストの途中から記述したいときの書き方を忘れていた。[1:5]で1~5の画像を取得という書き方もできる。

    # Jiff's original program
    # img = Image.open(os.path.join(dir_name,file)) # openはそのままの意味。path.join()で引数を結合してpathにしてくれる。dir_nameフォルダからオープン。
    # img_resize = img.resize((600,337)) # 今回はサイズ指定。アスペクト比固定でリサイズするのが目標。
    # img_resize.save(os.path.join(new_dir_name,file)) # 変数を引数のpathに保存。今回はnew_dir_name に保存。

    # Instead of above, use yuu-eguci's function
    original_path = os.path.join(dir_name, file)
    destination_path = os.path.join(new_dir_name, file)
    print(f'Use yuu-eguci function!! {original_path} -> {destination_path}')
    generate_thumbnail_360x195(original_path, destination_path)


