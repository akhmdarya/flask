
data_output = list()

def wordlist(data):
    data_output.clear()
    f = open(data,"r",encoding="utf-8")
    for line in f:
        data_output.append(line.replace('\n','').replace(' ',''))
    f.close()
    return data_output

