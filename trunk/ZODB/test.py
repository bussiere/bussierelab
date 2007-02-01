from ZODB import FileStorage, DB 
import transaction


storage = FileStorage.FileStorage('test-filestorage.fs')
db = DB(storage)
connection = db.open()
root = connection.root()
root['employees'] = ['Mary', 'Jo', 'Bob']
transaction.commit()
print root.items()
connection.close()


