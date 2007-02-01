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
test = User()
newuser.id = 'amk' 
newuser.first_name = 'Andrew'
newuser.last_name = 'Kuchling'
root[newuser.id] = newuser
transaction.commit()
print root.items()
test = root['amk']
print test.first_name
connection.close()


