import shelve

db = shelve.open('dict')
db['num']  = 1
# print(db['num'])
db.close()
