import shelve

db = shelve.open('dict')
# db['num']  = 50
# db['num2'] = 5000
# db['d'] = 0
print(db['225'])
db.close()
#
#
# num = 1
# n2 = 2
# n3 = 3
#
# l = [num,n2,n3]
#
# n =[]
# for i in l:
#     n.append(i)



















