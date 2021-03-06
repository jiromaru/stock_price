# STOCK_PRICE
Yahoo!ファイナンス上の株価データをWebスクレイピングによって取得し、MySQLに格納するツール

## 概要
株価のデータを収集するツール。get_stock.pyを実行すると各種パラメータ入力画面と上場している企業の一覧が出力される(下記画像参照)。そこから取得したい銘柄を選択(複数可)→実行すると選択したデータがMySQLに格納される。テーブルの名前は"銘柄名_期種"(例：極洋(1301)を月次で選択した場合は1301_mとなる)。  
構造は以下のようになっている。  
①get_stock.pyを実行  
②[カブサポ](URL "http://kabusapo.com")より上場企業の銘柄と銘柄コードのcsvを取得(プログラムと同じディレクトリにstock_no.csvとして保存)  
③取得したcsvを読み込み、画面に表示する(画面はtkinterを使用)  
③画面より各種パラメータと選択された銘柄をget_data.pyに受け渡し、[yahoo!ファイナンス](URL "https://finance.yahoo.co.jp/")にてWebスクレイピングを開始  
③取得したデータをMySQLに格納  

## 環境
OS:Windows10  
MySQL:8.0.11  
言語:python3  
その他:MySQLに"finance"というデータベースを事前に用意(今後は、なければ作成するように改修予定)

使用モジュール(標準モジュール以外)
* BeautifulSoup
* PyMySQL
* requests
* selenium  

その他必要なもの:chromedriver

### 各プログラムの説明
* get_stock.py  
  下記のプログラムを呼び出すメインプログラム。MySQLとのセッションの立ちあげや切断も行う。一番初めにカブサポより銘柄名と銘柄コードを対応付けたcsvを取得し、保存する。二回目実行以降は保存したcsvから情報を取得する形となる。
* mk_display.py  
  MySQLとの接続に必要な各種パラメータおよび、取得したい銘柄名や期種を選択するための画面を作成する(tkinterを使用)。
* get_data.py
Yahoo!ファイナンスのデータをBeautifulSoupを用いてWebスクレイピングを行う。

### 使用方法
上記プログラムとchromedriver.exeを同じディレクトリに配置し、get_stock.pyを実行する。

### 実行画面
![実行画面](https://github.com/jiromaru/stock_price/blob/images/stock_images.png)
