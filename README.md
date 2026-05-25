# 毎朝天気通知システム

三重県松阪市の天気（天気概況・最高気温・最低気温）を毎朝6:00にLINEへ自動通知します。

## ファイル構成

```
├── main.py           # エントリーポイント
├── weather.py        # 天気情報の取得・パース
├── message.py        # 通知メッセージの整形
├── line_notify.py    # LINE Messaging API への送信
├── requirements.txt  # 依存パッケージ
├── .env.example      # 環境変数サンプル
└── .github/
    └── workflows/
        └── weather_notify.yml  # GitHub Actions スケジュール設定
```

## セットアップ

### 1. 必要なAPIキー・トークンを取得する

| 項目 | 取得場所 |
|------|----------|
| `WEATHER_API_KEY` | [OpenWeatherMap](https://openweathermap.org) で無料登録 → API Keys |
| `LINE_CHANNEL_ACCESS_TOKEN` | [LINE Developers](https://developers.line.biz) → Messaging API チャンネル → チャンネルアクセストークン |
| `LINE_USER_ID` | LINE Developers → Messaging API → Your user ID（`U`から始まる文字列） |

### 2. GitHub Secrets に登録する

GitHubリポジトリの `Settings > Secrets and variables > Actions` に以下を追加：

- `WEATHER_API_KEY`
- `LINE_CHANNEL_ACCESS_TOKEN`
- `LINE_USER_ID`

### 3. リポジトリにプッシュする

```bash
git init
git add .
git commit -m "initial commit"
git remote add origin https://github.com/<ユーザー名>/<リポジトリ名>.git
git push -u origin main
```

プッシュ後、毎朝6:00（JST）に自動実行されます。

## ローカルで動作確認する

```bash
pip install -r requirements.txt
cp .env.example .env
# .env に実際のキーを記入してから実行
python main.py
```

## 手動実行（GitHub上から）

GitHub リポジトリの `Actions` タブ → `毎朝天気通知` → `Run workflow` で即時実行できます。
