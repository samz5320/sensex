from notify_run import Notify
import requests
from bs4 import BeautifulSoup
import time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import smtplib
import pandas as pd

url1="https://www.google.com/finance"
url="https://economictimes.indiatimes.com/indices/sensex_30_companies"
headers={"User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36"}

def live():
    
    page=requests.get(url,headers=headers)

    soup=BeautifulSoup(page.content,'html.parser')
    title=soup.find(id="todaysData").get_text()
    print("points:",title.strip())
    sensex=soup.find(id="ltp").get_text()
    strsen=sensex
    flsen=float(sensex)
    
    
    print("at present sensex is at :",sensex)
    list=[]
   
    
    ms=soup.find("span",{"class":"live_status"}).get_text()
    print(ms.upper())
    mstatus=soup.find(id="headlines").get_text()
    print("current status of the market is : ",mstatus,ms.upper())
    
    
    
    page=requests.get(url1,headers=headers)
    
    if flsen <40000:
            notify=Notify()
            notify.send(f"current sensex value is{flsen}\n current  points is {title} ")
            send_mail()
    while(True):
        
        list.append(flsen)
        print(list)
        l2=np.array(list)
        
        
        
        
        i=0
        if len(l2)>1:
            
            graph=[l2]

        plt.plot(l2)
        plt.show()
        time.sleep(1)

def send_mail():
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('illythompco@gmail.com','fslxthvbyxbxhazb')

    subject = 'for more news and status of the market pls visit the below'
    body ='check the link \nhttps://economictimes.indiatimes.com/indices/sensex_30_companies \n https://www.google.com/finance \n http://www.moneycontrol.com/markets/indian-indices/'

    msg=subject+body
    
    server.sendmail(
        'illythompco@gmail.com',
        'sanjayam5320@gmail.com',
        msg

    )
    print("email has been sent")

    server.quit()     
        
#live()

def table():
    url="http://www.moneycontrol.com/markets/indian-indices/"
    content=requests.get(url)
    soup=BeautifulSoup(content.text,'html.parser')
    table=soup.find('table',{"class":"responsive"})
    l1=[]
    rows=table.find_all("tr")
    for row in rows:
        rowtext=row.get_text()
        table1=rowtext.split("\n")
        l1.append(table1)
    df=pd.DataFrame(l1)
    
    print(df)
    df.to_csv("money.csv",header=False,index=False)

table()

def hist():
    url="https://finance.yahoo.com/quote/%5EBSESN/history?p=%5EBSESN"
    content=requests.get(url)
    soup=BeautifulSoup(content.text,'html.parser')
    table=soup.find("table",{"class":"W(100%) M(0)"})
    l1=[]
    rows=table.find_all("tr")
    for row in rows:
        rowtext=row.get_text()
        table1=rowtext.split("\n")
        l1.append(table1)
    df=pd.DataFrame(l1)
    print(df)
    df.to_csv("svlaues.csv")
hist()

    
