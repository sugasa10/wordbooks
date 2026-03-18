from flask import Flask, render_template, jsonify, request
import os
import random

app = Flask(__name__)

BASE = os.path.dirname(__file__)
WORDS_DIR = os.path.join(BASE, "words")

words_list = []
index = 0
BATCH = 20

# --- 単語帳一覧 ---
def load_books():
    return [f.replace(".txt", "") for f in os.listdir(WORDS_DIR) if f.endswith(".txt")]

# --- 単語読み込み ---
def load_words(book):
    global words_list, index
    path = os.path.join(WORDS_DIR, book + ".txt")
    with open(path, encoding="utf-8") as f:
        words_list = [line.strip() for line in f if line.strip()]
    random.shuffle(words_list)
    index = 0

@app.route("/")
def home():
    return render_template("flash.html")

# 単語帳リスト取得
@app.route("/wordbooks")
def wordbooks():
    return jsonify(load_books())

# 単語帳読み込み
@app.route("/load", methods=["POST"])
def load_book():
    data = request.json
    book = data["book"]
    load_words(book)
    return jsonify({"status": "ok"})

# 無限スクロール用：次の20単語取得
@app.route("/next")
def next_words():
    global index
    result = []
    while len(result) < BATCH and len(words_list) > 0:
        if index >= len(words_list):
            random.shuffle(words_list)
            index = 0
        result.append(words_list[index])
        index += 1
    return jsonify(result)

# 単語削除
@app.route("/remove", methods=["POST"])
def remove_word():
    global words_list
    data = request.json
    w = data["word"]
    if w in words_list:
        words_list.remove(w)
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)