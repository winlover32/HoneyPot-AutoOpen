# HoneyPot-AutoOpen

自動でHoneygainのHoneyPotを自動で開きます

## Use

1. 設定ファイルのコピー

```sh
cp sample.env .env
```

2. `.env`にメールアドレス, パスワード, WebhookURLを設定

3. `main.py`をcrontab等で定期実行