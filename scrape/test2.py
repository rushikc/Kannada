
w2 = 'ಸಂತೋಷವಾಗಿಲ್ಲ'
p=1
uni = w2.encode('utf-8')

print(str(uni))
# exit()
if uni.__contains__(b'\xe0\xb2\xbf\xe0\xb2\xb2\xe0\xb3\x8d\xe0\xb2\xb2'):
    p = 1 - p
    print('y')