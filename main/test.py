import xlrd
import xlsxwriter
import letters as k
import lib2 as m
import time
def process(txt):
    for i in range(len(txt)):
        txt[i] = txt[i].replace('\n','')
    while '' in txt:
        txt.remove('')
    return txt


wb = xlrd.open_workbook("data/kannada.xlsx")
sheet = wb.sheet_by_index(0)
s1 = []
s2 = []
for i in range(sheet.nrows):
    s1.append(str(sheet.cell_value(i, 0)))
    s2.append(sheet.cell_value(i, 1))

print(len(s1))
print(len(s2))
s1 = process(s1)
res = m.check_sentiment(s1)

#print(len(res))
#print(len(s1))

for k in range(len(res)):
    if res[k] == 0:
        res[k]= 'happy'
    elif res[k] == 1:
        res[k]= 'sad'
    elif res[k] == 2:
        res[k]= 'angry'
    elif res[k] == 3:
        res[k]= 'fear'
    elif res[k] == 4:
        res[k]= 'surprise'
    elif res[k] == 5:
        res[k]= 'neutral'

tot = len(res)
tot1 = len(res)
for k in range(len(res)):
    if s2[k] != res[k]:
        tot -=1

print("=========================================================\n\n")
print('Total sentences : ',len(res))
print('\n')
print("Accuracy is : ",(tot/tot1)*100)
print('\n\n')
print("=========================================================\n\n")
