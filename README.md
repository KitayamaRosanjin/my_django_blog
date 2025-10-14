# Djangoブログシステム

Djangoフレームワークを使ったシンプルなブログアプリケーション。モデル、ビュー、テンプレート、認証を学習するために構築しました。

## 背景と目的
- DjangoのMTVパターンを実践し、Webアプリの全体像を理解。
- 仮想環境から始め、ORM (モデル)、Class-Based Views、フォーム、ユーザー認証を一通り実装。
- 拡張性を意識: タグや画像アップロードを将来追加可能。

## 技術スタック
- Django 5.2.7
- Python 3.13
- SQLite (開発DB)
- HTML/CSS (静的ファイル管理)

## 機能
- 記事一覧/詳細表示
- 新規記事作成 (ログイン必須)
- ユーザー認証 (ログイン/ログアウト)
- 管理画面 (/admin/) で記事編集

## セットアップ手順
1. リポジトリクローン: `git clone <repo-url>`
2. 仮想環境作成: `python -m venv venv`
3. アクティベート: `venv\Scripts\activate` (Windows)
4. 依存インストール: `pip install -r requirements.txt`
5. マイグレーション: `python manage.py migrate`
6. スーパーユーザー作成: `python manage.py createsuperuser`
7. サーバー起動: `python manage.py runserver`
8. ブラウザで http://127.0.0.1:8000/ アクセス

## 改善点
- 画像アップロード (Mediaファイル)
- APIエンドポイント (Django REST Framework)
- テストコード (unittest)

フィードバック歓迎！ Djangoの柔軟性を体感できました。
