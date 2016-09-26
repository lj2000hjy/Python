def readfile():
    fr=open('wformat.txt','r')
    while (1==1):
        line=fr.readline()
        if(line==''):
            break
        else:
            print line
    fr.close()