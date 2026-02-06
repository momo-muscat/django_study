# 【PostgreSQL】
```
user：postgres
password：5150
```

## ● psql接続
```
psql -U postgres -p 5432
```

## ● DB生成
```
CREATE DATABASE [DBname];
```

## ● 新しいユーザ（ロール）作成
```
CREATE ROLE [username] WITH LOGIN PASSWORD 'password';
```

## ● 指定したユーザ（ロール）にデータベースを作成する権限（CREATEDB）を付与
```
ALTER ROLE [username] CREATEDB;
```

## ● 指定したデータベース（DBname）の所有者（OWNER）を変更
```
ALTER DATABASE [DBname] OWNER TO [username];
```

## ● psql終了
```
quit
```


# 【Python】
## ● 仮想環境作成
```
cd django_study
python -m venv venv
```

## ● 仮想環境のアクティベート
```
venv\Scripts\activate
```

## ● 仮想環境のディアクティベート
```
deactivate
```

## ● インストール済みパッケージとバージョン書き出し
```
pip freeze > requirements.txt
```

## ● 書き出したrequirements.txtを一括インストール
```
pip install -r requirements.txt
```

## ● pipを最新版にアップデート
```
python.exe -m pip install --upgrade pip
```


# 【Django】
## ● Djangoをインストール
```
python -m pip install Django
```

## ● インストール確認
```
django-admin --version
```

## ● Djangoをアップデート
```
python -m pip install -U Django
```

## ● Djangoプロジェクトの作成
（最後のピリオドがないとプロジェクトフォルダが二重構造になる）
```
uv run django-admin startproject apl .
```

## ● 作成されたファイルの確認
```
tree /f
django_study/          # プロジェクトのルートディレクトリ  
├── manage.py          # 管理コマンド実行用スクリプト  
└── apl/               # プロジェクト設定ディレクトリ  
    ├── __init__.py    # Pythonパッケージとして認識させるファイル  
    ├── settings.py    # プロジェクトの設定ファイル  
    ├── urls.py        # URLディスパッチの定義  
    ├── asgi.py        # 非同期サーバ用の設定  
    └── wsgi.py        # 本番サーバ用の設定
```

## ● 開発サーバ起動
```
python manage.py runserver
http://127.0.0.1:8000/
```

## ● VSCodeでプロジェクトを開く
1.  VSCodeを起動
1. 「ファイル」→「フォルダーを開く」
1.  プロジェクトのルートディレクトリを選択
1. 「Ctrl + Shift + P」を押してコマンドパレットを開く
1. 「Python: Select Interpreter」と入力してインタプリタのパスを選択

## ● settings.pyで言語・タイムゾーンの設定変更
```
LANGUAGE_CODE = 'ja'
TIME_ZONE = 'Asia/Tokyo'
```

## ● settings.pyでtemplateフォルダの設定
```
TEMPLATES = [  
    {  
        ....,  
        'DIRS': [BASE_DIR / "templates"],  
        ....,  
    },  
]
```

## ● アプリケーションの作成
```
python manage.py startapp [アプリ名]
```

## ● アプリケーションの登録
setteings.pyのINSTALLED_APPSに追加
```
'[アプリ名].apps.[アプリ名_PascalCase]Config'
```

## ● psycopg2インストール
```
python -m pip install psycopg2
```

## ● setteings.pyでDB接続設定（PostgreSQL）
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'name',                  # PostgreSQLデータベース名
        'USER': 'user',                  # データベースユーザ名
        'PASSWORD': 'password',          # データベースパスワード
        'HOST': 'localhost',             # データベースホスト（IPアドレスまたはホスト名）
        'PORT': '5432',                  # データベースポート（デフォルトは5432）
        'OPTIONS': {
            'client_encoding': 'UTF8',
        },
        'TIME_ZONE': 'Asia/Tokyo',       # 日本時間の場合
        'USE_TZ': True,                  # タイムゾーンを有効にする
    }
}
```

## ● データベースの設計図を作成
```
python manage.py makemigrations
```

## ● データベースに反映
```
python manage.py migrate
```

## ● 管理者ユーザーの作成
```
python manage.py createsuperuser
user:doi
e-mail:
password:12345678
```

## ● migrateをやり直す
1. 過去のmigrate履歴を確認  
python manage.py showmigrations
1. テーブルを全て削除
1. appのmigrationsフォルダの中身を削除
1. migrate履歴の削除  
python3 manage.py migrate --fake [アプリ名] zero
1. 履歴が削除されたかを1と同様のコマンドで確認
1. 通常の手順でmigrateをやり直す

## ● urls.pyでURLの登録
```
from django.urls import path, include
urlpatterns = [
    ...,
    path('app名/', include('[app名].urls')),
]
```

## ● [アプリ名]フォルダ内にurls.pyを作成
```
from django.urls import path
 
urlpatterns = [
  
]
```

## ● templateフォルダの作成
```
[templates]フォルダ > [アプリ名]フォルダ
```


# 【Git / GitHub】
## ● 新規作成時
```
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/momo-muscat/django_study.git
git push -u origin main
```

## ● 更新時
```
git remote add origin https://github.com/momo-muscat/django_study.git
git branch -M main
git push -u origin main
```

