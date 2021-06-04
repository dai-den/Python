import os
import zipfile

# zipを剥がす

# userNameフォルダがあるフォルダの相対パス
# この下に個人名のフォルダ群
USERNAME_FOLDER = "./userNameFolder/"
# 学番フォルダを出力する相対パス
STUDENTNUMBER_FOLDER = './studentNumberFolder/'

# 無視するファイルのリスト
IGNORE_FILENAME_LIST = [
  # macでfinderからディレクトリをいじると'.DS_Store'ができるので、それを抜かす
  '.DS_Store'
]

# 想定フォルダ構成
# 以下nは自然数
# 
# 学籍番号でフォルダを作って,中に01,02.c,...,n.c
# 学籍番号のフォルダをzipで固める
# 
# saiten1.py
# └ USERNAME_FOLDER
#    ├ userName_1(個人名フォルダ)
#    |  └ 学番.zip
#    |     └ 学番(学番.zipを解凍したフォルダ)
#    |        ├ 01.c
#    |        ├ 02.c
#    |       ・
#    |       ・
#    |       ・
#    |        └  n.c
#    ├ userName_2
#    └ userName_3
#    ・
#    ・
#    ・
#    └ userName_n 

if __name__ == "__main__":
  if(not os.path.exists(USERNAME_FOLDER)):
    print(USERNAME_FOLDER + "がないよ")
    exit

  # USERNAME_FOLDER以下の個人名のフォルダ群を取得する
  folders = os.listdir(USERNAME_FOLDER)

  # フォルダ構成関連で弾かれたフォルダの名前を記録する
  result_file_path = './saiten1-result.txt'

  # すべてのフォルダを見ていく
  for folder in folders:
    # もしも読み飛ばすファイルのリストに入っていれば次のファイルへ
    if(folder in IGNORE_FILENAME_LIST):
      continue

    # 個人名フォルダ以下のファイルをすべて取得
    zip_file = os.listdir(USERNAME_FOLDER + folder + '/')
    # 取得したファイル群から無駄なファイルを読み飛ばす
    zip_file = [f for f in zip_file if f not in IGNORE_FILENAME_LIST]

    # 個人名フォルダ直下はzipが一個しかないはずなので、違った場合エラーを吐く
    if(len(zip_file) != 1):
      f = open(result_file_path,'a')
      f.write(folder + " : 個人名フォルダ以下のファイルの数が違うよ" + '\n')
      f.close()
      continue

    # 学番を取得
    zip_file_name = (zip_file[0]).split('.zip')[0]

    file_err = False
    with zipfile.ZipFile(USERNAME_FOLDER + folder + '/' + zip_file[0]) as zip_src:
      # zipファイルの中身を見ていく(str型のlist)
      for file_name in zip_src.namelist():
        # file_name : zip以下のファイルの名前

        # zip以下のファイルの名前が学番で始まってないとおかしいので、エラーを吐く
        # ex) zip以下に直接0*.c(01.cを直接zipで固める)が入っているとエラー
        if(not (file_name.startswith(zip_file_name))):
          f = open(result_file_path,'a')
          f.write(folder + " : zipファイル以下がおかしいよ" + '\n')
          f.close()
          file_err = True
          break

    # zip以下のファイル名がおかしかった
    if(file_err):
      continue

    # 最終的にエラーがなければSTUDENTNUMBER_FOLDERにzip以下のファイル(学籍番号フォルダ)を移動
    with zipfile.ZipFile(USERNAME_FOLDER + folder + '/' + zip_file[0]) as zip_src:
      zip_src.extractall(STUDENTNUMBER_FOLDER)
  
  f = open(result_file_path,'a')
  f.write('================================' + '\n')
  f.close()