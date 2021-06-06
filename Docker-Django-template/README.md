# Django + Dockerテンプレート

注意事項として、pipでpsycopg2を追加する必要がある。

また、docker-composeでpostgresの環境変数を明示的に宣言しておかないと、通信が行えない。

## プロジェクト作成 

```Bash
docker-compose run web django-admin.py startproject composeexample .
```

でコンテナを作って内部でDjangoプロジェクトを作成する。

## データベース設定

startprojectの下にあるsettings.pyのDATABASESを

```Bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'db',
        'PORT': 5432,
    }
}
```

のように書き換える。

## コンテナ立ち上げ

```Bash
docker-compose up
```

docker-composeでpostgresのパスワードを宣言しないとここでエラーが出る。