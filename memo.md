# Python仮想環境

## 仮想環境の有効化
python -m venv scraping

## 仮想環境の起動
<venv>/scraping/Script/active.bat

※Linux環境は、別の手順で有効化する必要がある


# Pythonパッケージのインストール

pip list
pip install bs4
pip install requests


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

* 参考 *
<https://qiita.com/colorrabbit/items/6c3e96c394bb0f753ea0>


# ユニットテスト