import smtplib
import requests
from bs4 import BeautifulSoup
url = "https://ssc.nic.in/"
r = requests.get(url)
html_content = r.content
soup = BeautifulSoup(html_content, 'html.parser')

container = soup.findAll("div", {"class": "eachNotification"})
i = 0
msg = " "
for x in container:
    date = x.span.text
    news = x.a.text.strip()
    link = x.a.get('href')
    print(date)
    print(news)
    print(link)
    msg = msg+date+'\n'+news+'\n'+link+'\n'+'\n'
    i += 1
    if i == 10:
        break
sendmail("ayuagg27@gmail.com", msg)

