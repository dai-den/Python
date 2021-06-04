import os
import subprocess
from subprocess import PIPE

# cプログラムを実行する

# 学番フォルダが集まるフォルダの相対パス
STUDENTNUMBER_FOLDER = "./studentNumberFolder/"

# 実行結果を出力するファイルの名前
result_file_name = 'saiten2-result.txt'

# 無視するファイルのリスト
IGNORE_FILENAME_LIST = [
  # macでfinderからディレクトリをいじると'.DS_Store'ができるので、それを抜かす
  '.DS_Store',
  # フォルダ内で2つ目のプログラムを実行するときに,すでにできているファイルは読み飛ばす
  result_file_name,
  # コンパイル済みファイルは読み飛ばす
  'a.out'
]

COMPILE_OPTION = [
  '-lm',
  '',
  '',
  '',
  '',
  '',
]

# 想定フォルダ構成
# 以下nは自然数
# 
# 学籍番号でフォルダを作って,中に01,02.c,...,n.c
# 
# saiten2.py
# └ STUDENTNUMBER_FOLDER
#    ├ 学番フォルダ(学番.zipを解凍したフォルダ)
#    |  ├ 01.c
#    |  ├ 02.c
#    |  ・
#    |  ・
#    |  ・
#    |  └  n.c
#    ├ 学番フォルダ
#    └ 学番フォルダ
#    ・
#    ・
#    ・
#    └ 学番フォルダ
# 
# 最終的にそれぞれの学番フォルダに結果のtxtファイルが入る

if __name__ == "__main__":

  if(not os.path.exists(STUDENTNUMBER_FOLDER)):
    print(STUDENTNUMBER_FOLDER + "がないよ")
    exit

  # STUDENTNUMBER_FOLDER以下の学番フォルダ群を取得する
  folders = os.listdir(STUDENTNUMBER_FOLDER)

  # 学番フォルダを全て見ていく
  for folder in folders:
    # もしも読み飛ばすファイルのリストに入っていれば次のファイルへ
    # folderはフォルダ名=学番
    if(folder in IGNORE_FILENAME_LIST):
      continue

    # 結果を出力するファイルのパス(個別の学番フォルダの下)
    result_file_path = STUDENTNUMBER_FOLDER + folder + '/' + result_file_name

    # 実行結果を出力するファイルを作成する、学番で上書き
    f = open(result_file_path,'w')
    f.write(folder + '\n')
    f.close()

    # ソースファイルのファイル名をリストで取得して,ソートする
    sourcefiles = os.listdir(STUDENTNUMBER_FOLDER + folder + '/')
    sourcefiles.sort()

    # ソースファイルと同じディレクトリまで移動
    os.chdir(STUDENTNUMBER_FOLDER + folder + '/')

    # 区切りを結果ファイルに書き込む
    subprocess.run('echo ' + '================================' + ' >> ' + result_file_name,shell=True)

    # ソースファイルを一つずつ実行していく
    for sourcefile in sourcefiles:
      # もしも読み飛ばすファイルのリストに入っていれば次のソースファイルへ
      if(sourcefile in IGNORE_FILENAME_LIST):
        continue

      # ファイル名が.cで終わっているものや.c.cになっているものを弾く
      if((not sourcefile.endswith('.c')) or sourcefile.endswith('.c.c')):
        f = open(result_file_name,'a')
        f.write(sourcefile + " : ファイル名がおかしいよ" + '\n')
        f.write('================================' + '\n')
        f.close()
        continue
      
      # ソースファイルの番号からコンパイルオプションのリストのインデックスに変換
      option_number = int((sourcefile.split('.'))[0]) - 1

      # ファイル名を結果ファイルに書き込む
      f = open(result_file_name,'a')
      f.write(sourcefile + '\n')
      f.close()

      # コンパイル
      res = subprocess.run('gcc ' + sourcefile + ' ' + COMPILE_OPTION[option_number],stdout=PIPE, stderr=PIPE,shell=True)
      # コンパイルコマンドを出力する
      f = open(result_file_name,'a')
      f.write('gcc ' + sourcefile + ' ' + COMPILE_OPTION[option_number] + '\n\n')
      f.close()

      if(res.stderr != ""):
        # コンパイルエラーは結果ファイルに'コンパイルエラー'と書き込む
        f = open(result_file_name,'a')
        f.write('コンパイルエラー ' + '\n')
        f.close()
      else:
        # うまくコンパイルできたら実行結果を結果ファイルに書き込む
        res = subprocess.run('./a.out >> ' + result_file_name,stdout=PIPE, stderr=PIPE,text=True,shell=True)

      # 区切りを結果ファイルに書き込む
      f = open(result_file_name,'a')
      f.write('================================' + '\n')
      f.close()
    
    # 元のディレクトリに戻る
    os.chdir('../../')