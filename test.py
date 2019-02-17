from Kannada.kannada import letters as k
# from Kannada.kannada.letter import init
import shelve
# k = init()
# k.assign()

db = shelve.open('link')
l_links = db['l3_links']
db.close()


print(k.a)
print(len(k.klist))
print(l_links)
