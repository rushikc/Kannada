import re
# from Kannada.kannada import letters as k
import letters as k

import time
fh = open('data/comment.txt','r')
txt = fh.readlines()
fh.close()

stop_words = k.stop_words

def negation(neg):
    if neg.__contains__(b'\xe0\xb2\xbf\xe0\xb2\xb2\xe0\xb3\x8d\xe0\xb2\xb2'):
        return True
    else:
        return False

def tenses(uni,p):
    for kk2 in k.past_future:
        if uni.__contains__(kk2):
            p=p*0.7
            return p
    return p

def check_sentiment(txt):
    arr = []
    time.sleep(1)
    for i in range(len(txt)):
        
        words = []
        chappy = 0
        csad = 0
        csurprise = 0
        cangry = 0
        cfear = 0 
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

        while '' in words:
            words.remove('')

        
        prob=[0,0,0,0,0]

        if (len(words)):
            print(words)
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
                        
                        p= tenses(uni,p)
                        
                        if p > 0.5:
                            chappy+=1
                        if prob[num] == 0:
                            prob[num] = p
                        else:
                            prob[num] = (prob[num]+p)/2
                        hw = w2



                        # print(prob)



                for w2 in k.sad:
                    # print(w2)
                    if w1.__contains__(w2):
                        num=1
                        p = k.dsad[w2]
                        p = p[2]
                        uni = w1.encode('utf-8')
                        if uni.__contains__(b'\xe0\xb2\xbf\xe0\xb2\xb2\xe0\xb3\x8d\xe0\xb2\xb2'):
                            p = 1 - p

                        p= tenses(uni,p)
                        if p > 0.5:
                            csad+=1
                        if prob[num] == 0:
                            prob[num] = p
                        else:
                            prob[num] = (prob[num]+p)/2
                        sw = w2

                        # print(prob)

                for w2 in k.angry:
                    # print(w2)
                    if w1.__contains__(w2):
                        num=2
                        # print('in')
                        p = k.dangry[w2]
                        p = p[2]
                        uni = w1.encode('utf-8')
                        if uni.__contains__(b'\xe0\xb2\xbf\xe0\xb2\xb2\xe0\xb3\x8d\xe0\xb2\xb2'):
                            p = 1 - p

                        p= tenses(uni,p)
                        if p > 0.5:
                            cangry+=1
                        if prob[num] == 0:
                            prob[num] = p
                        else:
                            prob[num] = (prob[num]+p)/2
                        # print(prob)
                        sw = w2

                        # print(prob)

                for w2 in k.fear:
                    # print(w2)
                    if w1.__contains__(w2):
                        num=3
                        p = k.dfear[w2]
                        p = p[2]
                        uni = w1.encode('utf-8')
                        if uni.__contains__(b'\xe0\xb2\xbf\xe0\xb2\xb2\xe0\xb3\x8d\xe0\xb2\xb2'):
                            p = 1 - p
                        
                        p= tenses(uni,p)
                        if p > 0.5:
                            cfear+=1
                        if prob[num] == 0:
                            prob[num] = p
                        else:
                            prob[num] = (prob[num]+p)/2
                        aw = w2

                        # print(prob)
                for w2 in k.surprise:
                    # print(w2)
                    if w1.__contains__(w2):
                        num=4
                        p = k.dsurprise[w2]
                        p = p[2]
                        uni = w1.encode('utf-8')
                        if uni.__contains__(b'\xe0\xb2\xbf\xe0\xb2\xb2\xe0\xb3\x8d\xe0\xb2\xb2'):
                            p = 1 - p
                        
                        p= tenses(uni,p)
                        if p > 0.5:
                            csurprise+=1
                        if prob[num] == 0:
                            prob[num] = p
                        else:
                            prob[num] = (prob[num]+p)/2
                        aw = w2

                        # print(prob)


            
            tot = chappy+csad+cangry+csurprise+cfear
            if(tot==0):
                tot=1
            
            ann = [chappy,csad,cangry,cfear,csurprise]
            # print(prob)
            # print(ann)
            for pp1 in range(len(prob)):
                prob[pp1] = (prob[pp1]*ann[pp1])/tot

            mi  = max(prob)
            ind = prob.index(mi)
            
            
            # print(ind)
            # print(prob)
            if mi == 0:
                print('Neutral')
                arr.append(5)
            else:
                if ind == 0:
                    print('Happy')
                    arr.append(0)
                if ind == 1:
                    print('Sad')
                    arr.append(1)
                if ind == 2:
                    print('Angry')
                    arr.append(2)
                if ind == 3:
                    print('Fear')
                    arr.append(3)
                if ind == 4:
                    print('Surprise')
                    arr.append(4)
        else:
            arr.append(5)
    return arr





