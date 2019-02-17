from Kannada.kannada import letters as k
# from Kannada.kannada.letter import init
import shelve
# k = init()
# k.assign()

db = shelve.open('link.db')
l_links = db['l_links']
db.close()


print(k.a)
print(len(k.klist))
