from flask import Flask, url_for
from markupsafe import escape
from flask_cors import CORS
from requests.models import Response

app = Flask(__name__)
CORS(app)


@app.route('/parse/<url>')
def profile(url):
    return main('http://'+url)

with app.test_request_context():
    print(url_for('profile', url='John Doe'))

 
from words import wordlist
from search import findURL
from virustotal import AntiVirus

import json
import os
import requests
import urllib.request
import re
from bs4 import BeautifulSoup



array = [["Banner","False"],["Privacy_link","False"]]


#div-banner list
data_div_list = list()

#url-privacy list
data_url_list = list()


#privacy-link list
privacy_list = list()
data_privacy_list = list()
dataJson = ' { "Banner":"False", "Privacy_link":"null", "Article_6 ( Lawfulness of processing)":"False", "Contact":"False", "Period":"False", "Third_parties":"False", "Result": "null"} '
x = json.loads(dataJson)
symbol = ".;"

#Sort list function
def sort_list(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]


#Main fucnction
def main(url):
   
    data_div_list.clear()
    data_url_list.clear()
    privacy_list.clear()
    data_privacy_list.clear()


    privacy_link = ''
  
    #create wordlist
    data_div_list.extend(wordlist("db\\div_db\\div_db.txt"))
    data_url_list.extend(wordlist("db\\link_db\\link_db.txt"))
    #url request
    # response = requests.get(url)
    try:
        response=requests.get(url)
    except:
        response=requests.get('http://'+url)
    

    #html parser
    soup = BeautifulSoup(response.text, 'html.parser')
    

    #link parser
    mylinks = soup.find_all('a')
    #div parser
    mydivs = soup.find_all('div')

    #output div-banner
    for banner in mydivs:
        for div in data_div_list:
            if(str(banner).find(div)>0):
                array[0][1]="True"


    #privacy link cheker
    for link in mylinks:
        for line in data_url_list:
            link_ = str(link)
            # link_ = str(link).replace('https'," ").replace('/'," ")
            # link_ = str(link).replace('http'," ").replace('/'," ")
            print(link_+'^^^^^^^^^^^^^^^^^^^^^^^^^')
            if(link_.find(line)>0):
                privacy_list.extend(findURL(str(link), url))
              
    
    #request privacy_link
    if(len(privacy_list)!=0):
        #list sort
        data_privacy_list.extend(sort_list(privacy_list))
        if(len(data_privacy_list)):
            array[1][1] = 'True'
        for link_ in privacy_list:
            for line in data_url_list:
                if(link_.find(line)>0):
                    privacy_link = str(link_).replace('\n',"")
                    break
            if(breakpoint):
                break
    
    if(privacy_link):
        x["Privacy_link"]=privacy_link
        return str(karina(privacy_link))
    return x
   
#----------------------------------------------------------------

#----------------------------------------------------------------
def karina(privacy_link):
    if(privacy_link[0:4]!='http'):
        privacy_link='http://'+privacy_link

    #url request
    response = requests.get(privacy_link)
    soup = BeautifulSoup(response.text, 'html.parser')
    my_ul_li = soup.find_all('ul')

    files = next(os.walk('db\\text_db'))[2]  
    dir = 'db\\text_db\\'
    for f in files:
        count=0
        dataDB = wordlist(dir+f)
        f=f.replace('.txt',"")

        for p in my_ul_li:
            count=0
            for data in dataDB:
                if(str(p).find(data)>0):
                    count=count+1

            if(count>=(len(dataDB)/3)):
                x[f]="True"
                break
        if(count<(len(dataDB)/3)): 
            x[f]="False"
    return x