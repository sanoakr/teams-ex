# teams-ex
Convert Teams assignment xlsxl file to user score csv.
Teams課題の成績エクセルファイルからユーザーごとの配点csvへ変換する
## Requirements
- Python3
- Pandas
## How to use
> python3 teams-ex.py Teams成績ファイル.xlsx
-  Microsoft Teams で Education_Calss テンプレートで作成されたチームの成績一覧 xlsx からユーザごとの成績テーブルを csv として出力します。
- 入力はクラスチームの一般チャネル上部タブ「成績」の「Excelにエクスポート」から取得できる xlsx ファイル
- ユーザ名としてメールアドレスからドメインを削除したものを利用しています。replace で固定ドメイン削除しているので、split('@')[0] とかの方がよいかもしれません。
- 各課題提出状況から得点への変換は score 辞書で定義しているので適宜変更してください。
