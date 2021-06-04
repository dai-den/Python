import os
import subprocess
from subprocess import PIPE

# 学番フォルダが集まるフォルダの相対パス
dir = "./studentNumberFolder/"

if __name__ == "__main__":
  folders = os.listdir(dir)

  for folder in folders:
    # macでfinderからディレクトリをいじると'.DS_Store'ができるので、それを抜かす
    if(folder == '.DS_Store'):
      continue

    # 結果を出力するファイルのパス
    result_file_path = dir + folder + '/result.txt'

    # 結果ファイルを作成する、学番で上書き
    f = open(result_file_path,'w')
    f.write(folder + '\n')
    f.close()

    # ソースファイルのファイル名をリストで取得してソート
    sourcefiles = os.listdir(dir + folder + '/')
    sourcefiles.sort()

    # ソースファイルと同じディレクトリまで移動
    os.chdir(dir + folder + '/')

    # 区切りを結果ファイルに書き込む
    subprocess.run('echo ' + '================================' + ' >> result.txt',shell=True)

    for sourcefile in sourcefiles:
      if(sourcefile == '.DS_Store' or sourcefile == 'result.txt' or sourcefile == 'a.out'):
        continue
      # ファイル名が.cで終わってないのはおかしい
      if(not sourcefile.endswith('.c')):
        print(sourcefile + "はファイル名がおかしいよ")
        continue
      
      # echoでファイル名を結果ファイルに書き込む
      subprocess.run('echo ' + sourcefile + '>> result.txt',shell=True)
      # コンパイル
      res = subprocess.run('gcc ' + sourcefile,stdout=PIPE, stderr=PIPE,text=True,shell=True)
      # コンパイルエラーは結果ファイルに'コンパイルエラー'と書き込む
      if(res.stderr != ""):
        subprocess.run('echo ' + 'コンパイルエラー' + ' >> result.txt',shell=True)
      # 実行結果を結果ファイルに書き込む
      res = subprocess.run('./a.out >> result.txt',stdout=PIPE, stderr=PIPE,text=True,shell=True)
      # 区切りを結果ファイルに書き込む
      subprocess.run('echo ' + '================================' + ' >> result.txt',shell=True)
    
    # 元のディレクトリに戻る
    os.chdir('../../')