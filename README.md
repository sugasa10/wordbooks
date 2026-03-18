wordbooks 📚
単語帳をブラウザ上でフラッシュカード形式で学習できる、シンプルな Web アプリです。
概要
テキストファイルに単語を書いておくだけで、ブラウザからランダム順に単語を表示・学習できます。  
無限スクロールで次々と単語が流れ、覚えた単語はその場で削除できます。
機能
📂 単語帳選択 — `words/` フォルダ内の `.txt` ファイルを自動で一覧表示
🔀 シャッフル表示 — 単語をランダムな順番で表示（全単語を表示し終えると再シャッフル）
♾️ 無限スクロール — 20 単語ずつ順次読み込み
❌ 単語削除 — 覚えた単語をセッション中に非表示にする
ディレクトリ構成
```
wordbooks/
├── server.py           # Flask サーバー（メインロジック）
├── words/              # 単語帳テキストファイル置き場
│   └── *.txt           # 1行1単語で記載
├── templates/
│   └── flash.html      # フロントエンド（HTML）
├── static/             # CSS / JS などの静的ファイル
├── words.txt           # （サンプル or デフォルト単語リスト）
└── server_words.txt    # （サーバー用単語リスト）
```
セットアップ
必要なもの
Python 3.x
Flask
インストール
```bash
git clone https://github.com/sugasa10/wordbooks.git
cd wordbooks
pip install flask
```
使い方
1. 単語帳を用意する
`words/` フォルダに `.txt` ファイルを作成し、1 行に 1 単語ずつ記載します。
```
# words/英単語.txt の例
apple
banana
cherry
```
2. サーバーを起動する
```bash
python server.py
```
ブラウザで `http://localhost:5000` にアクセスします。
3. 学習する
画面上から学習したい単語帳を選択
単語がランダム順に表示される
覚えた単語は削除ボタンで非表示にできる
全単語を表示し終えると自動でシャッフルして繰り返す
API エンドポイント
メソッド	パス	説明
`GET`	`/`	メイン画面を表示
`GET`	`/wordbooks`	単語帳一覧を JSON で返す
`POST`	`/load`	単語帳を読み込む（`{"book": "ファイル名"}`）
`GET`	`/next`	次の 20 単語を JSON で返す
`POST`	`/remove`	指定した単語を削除（`{"word": "単語"}`）
技術スタック
バックエンド: Python / Flask
フロントエンド: HTML / CSS / JavaScript
ライセンス
このプロジェクトにはライセンスが明記されていません。使用の際はリポジトリオーナーに確認してください。
