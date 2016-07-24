このスクリプトは、長月達平先生のＲｅ：ゼロから始める異世界生活　web版txtファイルをダウンロードするためのツールである。
原稿は日本語のため、本説明も日本語で書かせていただきます。

■Shellスクリプト機能説明
□RE_download.bash
①自動にtxtファイルを順次ダウンロード
②ファイル名は数字です

□REtxt_mix.bash
①上記ダウンロードした多数txtファイルをひとつのファイルにまとめ

■Shell実行環境
　Ubuntu 12.04 LTS
　基本linux環境全部OKの認識です。
　※ubuntuの場合、デフォルトはbashではなくdashので、一度sudo dpkg-reconfigure dashによる変更が必要、Noを選べてください。
　　実施しないと、文法エラー頻発の恐れがあります。

■Pythonスクリプト機能説明
□RE_download.py
基本shell版と同様、ただし、reporthook追加によって、ダウンロードのパーセンテージ化を実現。

■Python実行環境
 python 2.7