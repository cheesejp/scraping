# Python仮想環境

## 仮想環境の有効化
```
python -m venv scraping
```
## 仮想環境の起動
```
<venv>/scraping/Script/active.bat
```
※Linux環境は、別の手順で有効化する必要がある


# Pythonパッケージのインストール
```
pip list
pip install bs4
pip install requests
```

# Pycharmの仮想環境(venv)の適応

* File->Settings
* Project:XXX->ProjectInterrupter
* Pythonの仮想環境のパスが選択できるので、選択しOKをクリック

# githubへSSH接続
1. 共通鍵の作成
```
ssh-keygen -t rsa -C "your_email@example.com"`
ssh-add ~/.ssh/id_rsa
```

2. ssh-add実行時に以下のエラーが発生する場合
```
Could not open a connection to your authentication agent.
```
その時は以下のおまじないを実行する。
```
eval `ssh-agent`
```

3. テスト
```
ssh -T git@github.com
```

* 参考 <https://qiita.com/colorrabbit/items/6c3e96c394bb0f753ea0>


# ユニットテスト

* テストディレクトリに__init__.pyを作成してモジュールとして認識させる必要がある。
* 検証メソッドはtest_検証メソッド名の命名規則にする。命名規則に一致するメソッドが自動的に実行される。
* テストは以下のコマンド
```
python -m unittest
python -m unittest test/hogehoge.py
```


