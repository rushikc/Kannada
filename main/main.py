import re
from Kannada.kannada import letters as k


fh = open('data/comment.txt','r')
txt = fh.readlines()
fh.close()

stop_words = k.stop_words


for i in range(len(txt)):
    txt[i] = txt[i].replace('\n','')

    words = str(txt[i])
    words = words.split(' ')
    for k in words:
        if k in stop_words:
            words.remove(k)


print(txt)
print(words)





