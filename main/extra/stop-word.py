

fh = open('../data/stop_words.txt','r')

txt = fh.readlines()

fh.close()

print(txt)

for i in range(len(txt)):
    st = str(txt[i])
    st = st.replace(' ','')
    st = st.replace('\n','')
    txt[i] = st
fh = open('../data/stop_word1.txt','w')

fh.writelines('l = [')
for k in txt:
    fh.writelines('\''+str(k)+'\',')

fh.writelines(']')
fh.close()