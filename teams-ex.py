#!/usr/bin/python3

import sys
import pandas as pd

# ファイル名をコマンドライン引数から取得
filename = sys.argv[1]

# エクセルファイル読み込み [氏名, メール アドレス, 課題, ステータス, フィードバック]
df = pd.read_excel(filename, header=1, usecols=[3,6,7,10,11])
df.replace('@mail.ryukoku.ac.jp', '', regex=True, inplace=True)

# ユーザーリスト
users = df['メール アドレス'].unique().tolist()

# 問題リスト
probs = pd.Series(data=df['課題'].unique())
print(probs)

# 総計用データフレーム
cols = pd.Series(data=['User'])
tdf = pd.DataFrame(index=[], columns=pd.concat([cols, probs]))

# ユーザーレコード追加
idx = 0
for u in users:
    tdf.loc[idx] = 0.0
    tdf.loc[idx, 'User'] = u
    idx += 1

# 得点を挿入
score = {
    '提出済み': 1.0,
    '再提出しました': 1.0,
    '遅れてオンにしました': 0.5,
    '返却済み': 0.25,
    '未提出': 0.0,
    '表示済み': 0.0
}
for row in df.itertuples():
    print(row)
    user = row._2
    prob = row.課題
    tdf.loc[tdf['User'] == user, prob] = score[row.ステータス]

# 総計を計算
tdf = pd.concat([tdf, pd.DataFrame(tdf.sum(axis=1, numeric_only=True),columns=['Total'])],axis=1)

# CSVに書き出し
print(tdf)
outname = filename.replace('.xlsx', '.csv')
tdf.to_csv(f'{outname}')
print(f"\nWrite out {outname}")
