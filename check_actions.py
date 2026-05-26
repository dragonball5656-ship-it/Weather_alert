import requests

r = requests.get("https://api.github.com/repos/dragonball5656-ship-it/Weather_alert/actions/runs?per_page=10")
runs = r.json().get("workflow_runs", [])

if not runs:
    print("実行履歴なし")
else:
    for run in runs:
        print(f'{run["created_at"]} | status: {run["status"]} | result: {run["conclusion"]}')
