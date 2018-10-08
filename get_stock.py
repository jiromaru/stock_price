##############################importの設定######################################
import urllib.request
import os
import pymysql
import sys
from mk_display import mk_display
from get_data import get_data

##############################パラメータの設定##################################
msg="正常"
stock_no_url="http://kabusapo.com/dl-file/dl-stocklist.php"
base_url="https://info.finance.yahoo.co.jp/history/?code="
stock_no_file="stock_no.csv"

if os.path.exists(stock_no_file) == False:
    urllib.request.urlretrieve(stock_no_url, stock_no_file)

param_list=mk_display(stock_no_file)

if len(param_list[3])==0:
    print("銘柄が選択されていません")
    sys.exit()

MySQL_param=param_list[0]
kisyu_list=param_list[1]
start_ym,fin_ym=param_list[2]
mei_no_list=param_list[3]

#MySQLの接続
conn=pymysql.connect(host = MySQL_param[0],port = int(MySQL_param[1]),user = MySQL_param[2],passwd = MySQL_param[3],db = "mysql")
cur=conn.cursor()
cur.execute("USE finance")

print("My_SQLパラメータ : \n" + "host : " + MySQL_param[0] + "/port : " + MySQL_param[1] + "/user : " + MySQL_param[2] + "/passwd : " + MySQL_param[3])
print("開始年 : " + start_ym,"終了年 : " + fin_ym)
print("期種 : " + ",".join(kisyu_list))

try:
    for mei_no in mei_no_list:
        for period in kisyu_list:
            cur.execute("CREATE TABLE IF NOT EXISTS finance.{0}_{1} (date CHAR(10),open INT,top INT,low INT,close INT,dekidaka BIGINT,close_adjust INT) ;".format(mei_no,period))
            cur.execute("CREATE TABLE IF NOT EXISTS finance.{0}_{1}_temp (date CHAR(10),open INT,top INT,low INT,close INT,dekidaka BIGINT,close_adjust INT);".format(mei_no,period))
            get_data(mei_no,base_url,start_ym,fin_ym,period,cur)
            cur.execute("INSERT INTO finance.{0}_{1} SELECT a.* from finance.{0}_{1}_temp a left join finance.{0}_{1} b on a.date=b.date where b.date IS NULL;".format(mei_no,period))
            cur.execute("DROP TABLE finance.{0}_{1}_temp".format(mei_no,period))
except:
    msg="異常"
finally:
    print(msg+"終了")
    cur.close()
    conn.close()
    
