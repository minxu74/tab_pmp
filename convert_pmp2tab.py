#!/usr/bin/env python


import sys

from bs4 import BeautifulSoup



def Convert(lst): 

    res_dct = {}
    for item in lst:
        res_dct[item.split(':')[0]] = item.split(':')[1]
    return res_dct 

with open("roadmap_historical_rms_xy.html") as fp:
    soup = BeautifulSoup(fp, features="lxml")


baseurl='https://oceanonly.llnl.gov/gleckler1/pptest/'

h1title=[]
for h1 in soup.find_all('h1'):
    h1title.append(h1.get_text())

links = []
value = []
varib = []
for se in soup.find_all('area'):
    ttp = se.get_attribute_list('tooltip')
    hrf = se.get_attribute_list('href')

    myarr = ttp[0].split("<br>")


    mydict = (Convert(myarr[0:-1]))

    temp = myarr[-1].split("<div id='thumbnail'><img src=")

    links.append((temp[-1][:-17]))

    value.append(float(temp[0].split(':')[1]))
    print (myarr[0:-2])
    print (Convert(myarr[0:-2]))
    print (float(temp[0].split(':')[1]))

    mydict.update({'value': float(temp[0].split(':')[1])})
    mydict.update({'link': temp[-1][:-17]})
    mydict.update({'href': hrf[0]})

    print (mydict['Variable'])
    #print (mydict)
     


