# テスト用フォルダ

## 想定する入力
  1. 学籍番号でフォルダを作って,中に01,02.c,...,n.c
  2. 学籍番号のフォルダをzipで固める(学籍番号.zip)
  3. 個人名のフォルダの中に学籍番号.zipを入れる

  という過程を経て,

  ```
  userName_1(個人名フォルダ)
   |  └ 学籍番号.zip
   |     └ 学籍番号フォルダ(学籍番号.zipを解凍したフォルダ)
   |        ├ 01.c
   |        ├ 02.c
   |        ・
   |        ・
   |        ・
   |        └  n.c
   ├ userName_2
   ├ userName_3
   ・
   ・
   ・
  ```

  という構成を想定しています.

  学籍番号.zipと学籍番号フォルダはそれぞれ各階層に1つのファイル/フォルダしか持たない構成です.

## プログラム実行前のフォルダ構成

  ```
  workFolder(適当なワークスペース)
  ├ saiten1.py
  ├ saiten2.py
  ├ userNameFolder
  |  ├ userName_1(個人名フォルダ)
  |  |   └ 学籍番号.zip
  |  |      └ 学籍番号フォルダ(学籍番号.zipを解凍したフォルダ)
  |  |         ├ 01.c
  |  |         ├ 02.c
  |  |         ・
  |  |         ・
  |  |         ・
  |  |         └  n.c
  |  |
  |  ├ userName_2(個人名フォルダ)
  |  ・
  |  ・
  |  ・
  |  └ userName_n(個人名フォルダ)
  └ studentNumberFolder
  ```

  適当なフォルダの下にsaiten1.pyとsaiten2.pyとuserNameFolder,studentNumberFolderを置いてください.

  userNameFolderには上で述べた個人名フォルダを入れてください.
  studentNumberFolderは空で大丈夫です.

## プログラム実行後のフォルダ構成

  ```
  workFolder
  ├ saiten1.py
  ├ saiten2.py
  ├ userNameFolder
  |  ├ userName_1(個人名フォルダ)
  |  |   └ 学籍番号_1.zip
  |  |      └ 学籍番号フォルダ_1(学籍番号.zipを解凍したフォルダ)
  |  |         ├ 01.c
  |  |         ・
  |  |         ・
  |  |         ・
  |  |         └  n.c
  |  ・
  |  ・
  |  ・
  |  └ userName_n(個人名フォルダ)
  ├ studentNumberFolder
  | ├ 学籍番号フォルダ_1
  | |         ├ 01.c
  | |         ・
  | |         ・
  | |         ・
  | |         ├ n.c
  | |         └ saiten2-result.txt
  | ├ 学籍番号フォルダ_2
  | ・
  | ・
  | ・
  | └ 学籍番号フォルダ_n
  |
  └ saiten1-result.txt
  ```

  saiten1.pyでstudentNumberFolder直下に学籍番号のフォルダ(zip)ファイルの中身がコピーされます.その過程でエラーを検知した場合はsaiten1-result.txtに記録します.

  saiten2.pyで学籍番号フォルダの中にあるCソースコードをコンパイル,実行して,saiten2-result.txtに結果を記録します.

## userNameFolder
  個人名フォルダを入れてください.

## studentNumberFolder
  saiten1.pyを実行すると,学籍番号.zipの中身の学籍番号フォルダをここにコピーします.
  (フォルダの個数等でエラーが出た場合はコピーされません)

  saiten2.pyを実行すると各学籍番号フォルダ内にsaiten2-result.txtが生成されます.

## saiten1-result.txt
  saiten1.pyを実行すると生成されます.
  zipファイルの中身をチェックしてエラーが出た場合はここに記録されます.

## saiten2-result.txt
  saiten2.pyを実行すると生成されます.
  cソースコードをコンパイルして実行した結果と,
  その過程で出たエラーを記録しています.

## 検知できるエラー
  saiten1.pyで判断する(saiten1-result.txtに記録が残る)
  - 個人名フォルダの下に複数個のファイルがある.(本来はzipファイル1つだけ)
  - 学籍番号.zip直下のフォルダ/ファイルが,学籍番号以外で始まっている(本来は学籍番号のフォルダがある)
  
  saiten2.pyで判断する(saiten2-result.txtに記録が残る)
  - ソースコードのファイル名が.cで終わっていない
  - ソースコードのファイル名が.c.cで終わっている
  - コンパイルエラー

## srcfile
  テスト用データがあります.
  studentNumber*内にcソースが有り,それをzipで固めたものを
  userName*フォルダに格納してあります.
  テストの際はuserName*フォルダをuserNameFolderに入れてください.

  - studentNumber1/02.c.cにソースファイルの名前の間違い
  - studentNumber1/03.cにコンパイルエラー
  - userName2/ 以下のファイルの数が多い(zipファイルが2つある)

  のエラーを仕込んであります.