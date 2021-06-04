import re

privacy_list = list()

#Check Url function
def findURL(row, url):
    try:
        privacy_list.clear()
        #url check regex
        entries=re.findall(r'(((https?:\/\/|www\.|\/\/)([\w.]+\/|)+[\w\-\_\=\&\.]+))', row)
        if(len(entries)!=0):
            for link in entries:
                _link = str(link[0])
                _link=_link[0:2].replace('//','')+_link[2:len(_link)]
                privacy_list.append(_link)
            return privacy_list

        #if the link is only to the directory 
        elif(len(entries)==0):
            entries=re.findall(r'(\/((\S*))\/)', row)
            for link in entries:
                #full link 
                findURL(url + str(link[0]),url)
        return privacy_list
    except:
        print(row)