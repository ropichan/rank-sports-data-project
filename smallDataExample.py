import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import japanize_matplotlib

# CSVファイルを読み込む
df = pd.read_csv('./data/smallDataExample.csv')

# 余分な空白を除去したチーム名に正規化
df['TeamAName'] = df['TeamAName'].astype(str).str.strip()
df['TeamBName'] = df['TeamBName'].astype(str).str.strip()

# すべてのチーム名を収集
all_teams = pd.unique(pd.concat([df['TeamAName'], df['TeamBName']], ignore_index=True))

# 集計用の辞書を初期化
team_stats = {
    team: {"勝ち数": 0, "負け数": 0, "引き分け数": 0}
    for team in all_teams
}

# 勝敗・引き分けを集計
for _, row in df.iterrows():
    a = row['TeamAName']
    b = row['TeamBName']
    sa = int(row['TeamAScore'])
    sb = int(row['TeamBScore'])

    if sa > sb:
        team_stats[a]["勝ち数"] += 1
        team_stats[b]["負け数"] += 1
    elif sa < sb:
        team_stats[a]["負け数"] += 1
        team_stats[b]["勝ち数"] += 1
    else:
        team_stats[a]["引き分け数"] += 1
        team_stats[b]["引き分け数"] += 1

# データフレーム化と追加列の計算
standings = pd.DataFrame([
    {
        "チーム名": team,
        "勝ち数": s["勝ち数"],
        "負け数": s["負け数"],
        "引き分け数": s["引き分け数"],
        "試合数": s["勝ち数"] + s["負け数"] + s["引き分け数"],
    }
    for team, s in team_stats.items()
])
standings["勝率"] = standings.apply(
    lambda r: (r["勝ち数"] / (r["勝ち数"] + r["負け数"])) if r["試合数"] > 0 else np.nan,
    axis=1,
)

# 表示（勝率・勝ち数で降順ソート）
standings = standings.sort_values(by=["勝率", "勝ち数"], ascending=[False, False], ignore_index=True)
print(standings)

# 保存
standings.to_csv('./data/standings.csv', index=False, encoding='utf-8-sig')

# グラフを作成
plt.figure(figsize=(10, 6))

# 勝率→勝ち数で降順ソート（同率の場合のタイブレーク付き）
standings_sorted = standings.sort_values(by=["勝率", "勝ち数"], ascending=[False, False]).reset_index(drop=True)

# 各チームの勝ち数、負け数、引き分け数を取得（明示的に配列化）
teams = standings_sorted["チーム名"].tolist()
wins = standings_sorted["勝ち数"].to_numpy()
losses = standings_sorted["負け数"].to_numpy()
draws = standings_sorted["引き分け数"].to_numpy()

# 勝ち数をプロット（一番左の層）
plt.barh(teams, wins, label="勝ち数", color='blue')

# 引き分け数を勝ち数の右に積み上げる
plt.barh(teams, draws, left=wins, label="引き分け数", color='red')

# 負け数を勝ち数と引き分け数の右に積み上げる
plt.barh(teams, losses, left=wins + draws, label="負け数", color='orange')


plt.xlabel("試合数")
plt.ylabel("チーム名")
plt.title("各チームの試合結果の内訳", pad=28)
ax = plt.gca()
ax.legend(title="結果", loc='upper right', bbox_to_anchor=(1.0, 1.18), ncol=3, frameon=False)
# 高勝率が上に来るようY軸を反転
plt.gca().invert_yaxis()
plt.gca().set_xlim(0, 20)
# 目盛り線を追加（視認性向上）
plt.grid(axis='x', linestyle='--', alpha=1)
# x軸を5刻みの主目盛に設定
plt.gca().xaxis.set_major_locator(MultipleLocator(5))
plt.tight_layout()
plt.show()