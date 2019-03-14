import requests
import os

# os.system('wget https://gimmeproxy.com/api/getProxy')
r = requests.get('https://gimmeproxy.com/api/getProxy')
contents = r.content

print(contents)
# contents = contents.split(',')
# IP = contents[8]
# PORT = contents[9]

# print(IP)
