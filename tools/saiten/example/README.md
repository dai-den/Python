# テスト用フォルダ

## 想定フォルダ構成
  1. 学籍番号でフォルダを作って,中に01,02.c,...,n.c
  2. 学籍番号のフォルダをzipで固める(学籍番号.zip)
  3. 個人名のフォルダの中に学籍番号.zipを入れる

  という過程を経て,

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
  
  という構成を想定しています.

## userNameFolder(個人名フォルダ)
  userName*/studentNumber*.zip/studentNumber*/01.c,02.c ... 
  という構成です.

  studentNumber*.zipとstudentNumber*はそれぞれの階層にフォルダが1つしかない想定です.

## studentNumberFolder(学番フォルダ)
  studentNumber*/01.c,02.c ... , saiten2-result.txt
  という構成です.

  saiten1.pyを経てstudentNumber*.zip以下のフォルダをコピーしています.
  (フォルダの個数等でエラーが出た場合はコピーされません)

  saiten2.pyを実行すると各studentNumberFolder内にsaiten2-result.txtが生成されます.

## saiten1-result.txt
  saiten1.pyを実行すると生成されます.
  各フォルダをチェックしてエラーが出た場合はここに記録されます.

## saiten2-result.txt
  saiten2.pyを実行すると生成されます.
  cソースコードをコンパイルして実行する過程で出たエラーを記録しています.s

## 検知できるエラー
  saiten1.py
  - userName


## srcfile
  テスト用データがあります.
  studentNumber*内にcソースが有り,それをzipで固めたものを
  userName*フォルダに格納してあります.
  テストの際はuserName*フォルダをuserNameFolderに入れてください.

  - studentNumber1/02.c.cにソースファイルの名前の間違い
  - studentNumber1/03.cにコンパイルエラー
  - userName2/ 以下のフォルダが多い(zipファイルが2つある)

  のエラーを仕込んであります.