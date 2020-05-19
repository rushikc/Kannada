import xlrd

wb = xlrd.open_workbook('kaggle/train_data.xlsx')
sheet = wb.sheet_by_index(0)

sentiment = []
data = []
for i in range(5000):
    str1 = str(sheet.cell_value(i, 0))
    str2 = str(sheet.cell_value(i, 1))
    sentiment.append(str1)
    
    for k in str2.split(' '):
        if k.__contains__('@'):
            str2 = str2.replace(k,'')
        if k.__contains__('http'):
            str2 = str2.replace(k,'')
    for char in str2:
        if char in "![]+-*/#$%^&@":
            str2.replace(char,'')
    
    data.append(str2)


import sys
import re

if (sys.version_info[0] < 3):
    import urllib2
    import urllib
    import HTMLParser
else:
    import html.parser
    import urllib.request
    import urllib.parse

agent = {'User-Agent':
"Mozilla/4.0 (\
compatible;\
MSIE 6.0;\
Windows NT 5.1;\
SV1;\
.NET CLR 1.1.4322;\
.NET CLR 2.0.50727;\
.NET CLR 3.0.04506.30\
)"}


def unescape(text):
    if (sys.version_info[0] < 3):
        parser = HTMLParser.HTMLParser()
    else:
        parser = html.parser.HTMLParser()
    return (parser.unescape(text))


def translate(to_translate, to_language="auto", from_language="auto"):

    base_link = "http://translate.google.com/m?hl=%s&sl=%s&q=%s"
    if (sys.version_info[0] < 3):
        to_translate = urllib.quote_plus(to_translate)
        link = base_link % (to_language, from_language, to_translate)
        request = urllib2.Request(link, headers=agent)
        raw_data = urllib2.urlopen(request).read()
    else:
        to_translate = urllib.parse.quote(to_translate)
        link = base_link % (to_language, from_language, to_translate)
        request = urllib.request.Request(link, headers=agent)
        raw_data = urllib.request.urlopen(request).read()
    data = raw_data.decode("utf-8")
    expr = r'class="t0">(.*?)<'
    re_result = re.findall(expr, data)
    if (len(re_result) == 0):
        result = ""
    else:
        result = unescape(re_result[0])
    return (result)

for k in range(len(data)):
    data[k] = translate(data[k],'kn','en')

fh = open('kannada3.csv','w')
for i in range(len(sentiment)):
    fh.write(sentiment[i]+'\t')
    fh.write(data[i]+'\n')
fh.close()
# print(sentiment)
# print(data)
