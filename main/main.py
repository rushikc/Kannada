import re
from Kannada.kannada import letters as k


fh = open('data/comment.txt','r')
txt = fh.readlines()
fh.close()

stop_words = k.stop_words


for i in range(len(txt)):
    words = []
    txt[i] = txt[i].replace('\n','')
    words = str(txt[i])
    words = words.split(' ')
    # print(words[1])
    for k1 in range(words.__len__()):
        if words[k1] in stop_words:
            words[k1] = ''
        if words[k1].__contains__('ಅಸಂತೋಷ'):
            ind = words.index(words[k1])
            # print('ye')
            words[ind] = words[ind].replace('ಅಸಂತೋಷ','ದುಃಖ')


    print(words)
    prob=[0,0,0,0,0]

    for w1 in words:
        # print(w1)
        for w2 in k.happy:
            # print(w2)
            if w1.__contains__(w2):
                num=0
                p = k.dhappy[w2]
                p = p[2]
                uni = w1.encode('utf-8')
                if uni.__contains__(b'\xe0\xb2\xbf\xe0\xb2\xb2\xe0\xb3\x8d\xe0\xb2\xb2'):
                    p = 1 - p

                if prob[num] == 0:
                    prob[num] = p
                else:
                    prob[num] = (prob[num]+p)/2
                hw = w2

                print(prob)



        for w2 in k.sad:
            # print(w2)
            if w1.__contains__(w2):
                num=1
                p = k.dsad[w2]
                p = p[2]
                uni = w1.encode('utf-8')
                if uni.__contains__(b'\xe0\xb2\xbf\xe0\xb2\xb2\xe0\xb3\x8d\xe0\xb2\xb2'):
                    p = 1 - p

                if prob[num] == 0:
                    prob[num] = p
                else:
                    prob[num] = (prob[num]+p)/2
                sw = w2

                print(prob)



# \xe0\xb2\xbf\xe0\xb2\xb2\xe0\xb3\x8d\xe0\xb2\xb2



