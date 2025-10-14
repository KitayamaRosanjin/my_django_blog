# Djangoブログシステム

Djangoフレームワークを使って構築したシンプルなブログポートフォリオプロジェクトです。Web開発の基礎（モデル、ビュー、テンプレート、フォーム、ユーザー認証）を学習するために作成しました。転職や副業の文脈ではなく、純粋な技術習得を目的としています。

## プロジェクトの背景と目的
- **学習動機**: Djangoの公式ドキュメントを基に、MTV（Model-Template-View）パターンを実際に実装。仮想環境構築から始め、ORMのクエリ、Class-Based Views、CSRF保護、ログイン認証までを一通り体験。
- **設計の考え方**:
  - シンプルさを優先: 記事のCRUD操作を中心に、拡張性を考慮（将来のコメント機能や画像アップロード可能）。
  - ベストプラクティス: マイグレーション管理、.gitignoreで環境分離、UTF-8エンコーディング徹底。
  - トラブルシューティング: エンコーディングエラーやテンプレートパスミスを解決し、堅牢性を確保。

## 技術スタック
- **バックエンド**: Django 5.2.7 (ORM, Views, Forms, Authentication)
- **フロントエンド**: HTML/CSS (静的ファイル管理, Bootstrap未使用で純粋Djangoテンプレート)
- **データベース**: SQLite (開発用)
- **環境**: Python 3.13 + venv (仮想環境)

## 機能概要
- **記事一覧/詳細表示**: 全ユーザーの記事を閲覧。空時は「まだ記事がありません」のメッセージ。
- **新規記事作成**: ログイン必須。著者を自動紐付け、保存後一覧に戻る。
- **ユーザー認証**: Django内蔵のログイン/ログアウト。未認証時は /login/ にリダイレクト。
- **管理画面**: /admin/ で記事CRUD可能（スーパーユーザー作成必須）。

<image-card alt="記事一覧スクショ" src="screenshot_post_list.png" ></image-card>  <!-- 後でローカルスクショを追加 -->
<image-card alt="記事作成フォーム" src="screenshot_post_form.png" ></image-card>

## セットアップ手順
1. リポジトリクローン: `git clone https://github.com/KitayamaRosanjin/my_django_blog.git`
2. ディレクトリ移動: `cd my_django_blog`
3. 仮想環境作成: `python -m venv venv`
4. アクティベート: `venv\Scripts\activate` (Windows) / `source venv/bin/activate` (macOS/Linux)
5. 依存インストール: `pip install -r requirements.txt`
6. マイグレーション: `python manage.py migrate`
7. スーパーユーザー作成: `python manage.py createsuperuser` (ユーザー名/パスワード入力)
8. サーバー起動: `python manage.py runserver`
9. ブラウザで http://127.0.0.1:8000/ にアクセス。ログイン後、記事作成テスト。

**注意**: 本番デプロイ時はDEBUG=Falseに変更し、SECRET_KEYを環境変数化。

## 今後の改善点
- 画像アップロード (Mediaファイル設定)。
- コメント機能 (Commentモデル追加)。
- API化 (Django REST Framework導入)。
- テストコード (unittestでビュー/モデルテスト)。

このプロジェクトを通じて、Djangoの柔軟性とエラーハンドリングを学びました。フィードバック歓迎です！

---

**作成日**: 2025年10月15日  
**作者**: KitayamaRosanjin
