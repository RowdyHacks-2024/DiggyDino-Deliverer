from inspect import getmembers, isroutine
from src.main import db

db.create_all()

class MyClass(object):
    a = '12'
    b = '34'
    def myfunc(self):
        return self.a

attributes = filter(
    lambda f: '_' not in f[0],
    getmembers(MyClass, lambda a: not (isroutine(a))),
)

attributes = dict(attributes)


print(attributes)
print('\n')

print(dict(attributes))
