from bs4 import BeautifulSoup
import requests

def get_data(mei_no,base_url,start_ym,fin_ym,period,cur):
    cnt=1
    end=0

    while True:

        if end == 1:
            break

        url=base_url + mei_no + ".T&sy=" + start_ym + "&sm=1&sd=1&ey=" + fin_ym + "&em=12&ed=31&tm=" + period + "&p=" + str(cnt)
        html=requests.get(url).text
        soup = BeautifulSoup(html, "html.parser")
        table_list=soup.find_all("table")

        for table in table_list:

            if "日付" in str(table):
                #項目名をheader_listとして取得しているが現在は使用していない。
                header_list=[i.string for i in table.find_all("th")]
                
                for j in table.find_all("tr"):
                    if "分割" in str(j):
                        continue
                    output_list=[]
                    for k in j.find_all("td"):

                        if "年" and "月" and "日" in str(k):
                            k=k.text.replace("年","/").replace("月","/").replace("日","")
                            output_list.append(k)
                            continue
                        
                        elif "年" and "月" in str(k):
                            k=k.text.replace("年","/").replace("月","")
                            output_list.append(k)
                            continue

                        elif "年" in str(k):
                            k=k.text.replace("年","")
                            output_list.append(k)
                            continue

                        output_list.append(k.text)
                    if output_list!=[]:
                        output_list=[out.replace(",","") for out in output_list]
                        cur.execute("INSERT INTO finance.{0}_temp VALUES ('{1[0]}',{1[1]},{1[2]},{1[3]},{1[4]},{1[5]},{1[6]});".format(mei_no+"_"+period,output_list))

                if output_list==[]:
                    end=1
                    break

        cnt+=1
