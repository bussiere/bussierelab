from ZODB import FileStorage, DB 
import transaction

test = """ storage = FileStorage.FileStorage('test-filestorage.fs')
db = DB(storage)
connection = db.open()
root = connection.root()
root['employees'] = ['Mary', 'Jo', 'Bob']
transaction.commit()
k =  root.items()
for l in k :
    print l
connection.close()
"""

from persistent import Persistent
class User(Persistent):
    pass

storage = FileStorage.FileStorage('test-filestorage.fs')
db = DB(storage)
connection = db.open()
root = connection.root()
newuser = User() 
neuser = User() 
test = User()
newuser.id = 'amk' 
neuser.id = 'ak' 
newuser.first_name = 'Andrew'
neuser.first_name = 'Andre'
newuser.last_name = 'Kuchling'
neuser.last_name = 'Kuch'
root[newuser.id] = newuser
root[neuser.id] = neuser
transaction.commit()
print root.items()
test = root['amk']
k = root.items()
for l in k :
    print l[1].first_name
print test.first_name
connection.close()


