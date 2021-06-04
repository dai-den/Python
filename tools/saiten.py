import os
import zipfile

# userNameフォルダがあるフォルダの相対パス
dir = "./userNameFolder/"
# 学番フォルダを出力する相対パス
output_dir = './studentNumberFolder/'

# userName/学番.zip/0*.cを想定している
if __name__ == "__main__":
  # dir以下のフォルダを取得する
  folders = os.listdir(dir)

  for folder in folders:
    # print(folder)
    # macでfinderからディレクトリをいじると'.DS_Store'ができるので、それを抜かす
    if(folder == '.DS_Store'):
      continue

    zip_file = os.listdir(dir + folder + '/')
    zip_file= [n for n in zip_file if n != '.DS_Store']
    # zip_file : userName以下のフォルダ構成のリスト

    # userName直下はzipが一個しかないはずなので、違った場合エラーを吐く
    if(len(zip_file) != 1):
      print(folder + " is bad : フォルダの数が違うよ")
      continue

    # 学番
    zip_file_name = (zip_file[0]).split('.zip')[0]

    flag_zip = False
    with zipfile.ZipFile(dir + folder + '/' + zip_file[0]) as zip_src:
      # zip_src.namelist()でzipの中身のstr型のlist
      for file_name in zip_src.namelist():
        # file_name : zip以下のファイルの名前

        # zip以下のファイルの名前が学番で始まってないとおかしいので、エラーを吐く
        # ex) zip以下に直接0*.cが入っているとエラー
        if(not (file_name.startswith(zip_file_name))):
          print(folder + " is bad : zipファイル以下がおかしいよ")
          flag_zip = True
          break

    # zip以下のファイル名がおかしかった
    if(flag_zip):
      continue

    # 最終的にエラーがなければoutput_dirにzip以下のファイルを移動
    with zipfile.ZipFile(dir + folder + '/' + zip_file[0]) as zip_src:
      zip_src.extractall(output_dir)
      

