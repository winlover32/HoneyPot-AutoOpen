# HoneyPot-AutoOpen

自動でHoneygainのHoneyPotを自動で開きます

## Use

1. 設定ファイルのコピー

```sh
cp sample.env .env
```

2. `.env`にメールアドレス, パスワード, WebhookURL(任意)を設定

3. 依存パッケージをインストール

```
poetry install
```

4. `main.py`をcrontab等で定期実行
