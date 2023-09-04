import os
from bs4 import BeautifulSoup

def main():
    list_div=[]

    for filename in os.listdir('source'):
        try:
            if filename.startswith(__name__.split('.')[-1]+'-'):
                html_doc='source/'+filename
                file=open(html_doc,'r')
                soup=BeautifulSoup(file,'html.parser')
                divs_name=soup.find_all('tr', {"class": "trow"})
                for div in divs_name:
                    title = div.find_all('td')[0].text.strip()
                    description = div.find_all('td')[2].text.strip()
                    link = div.find_all('td')[5].a['href']
                    list_div.append({"title" : title, "description" : description, "link": link, "slug": filename })
                file.close()
        except:
            print("Failed during : " + filename)
            pass
    print(list_div)
    return list_div
