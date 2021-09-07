
class BaseClass():
    def __init__(self):
        self.basic_sth = 0
    
    def print_self(self):
        print(type(self) ,'Functions will be inherited by default')
    
    def __lalala(self):
        print(type(self), 'it could not be inherited because you write __ in the functin name')
    
    @staticmethod
    def sfunc():
        print('this function do not needs self, because it belongs to Class, not object')
        print('call it by BasicClass.sfunc()')

class A(BaseClass):
    def __init__(self):
        super().__init__() # called __init__ of super class
        self.a_sth = 1

class B(BaseClass):
    def __init__(self):
        # if you do not write super().__init__() here, you can not use basic_sth from the baseclass
        self.b_sth = 2
    

c = BaseClass()
a = A()
b = B()

c.print_self()
a.print_self()
b.print_self()

BaseClass.sfunc()
# or you can use
a.sfunc()
b.sfunc()
c.sfunc()


print('try to check elements')

print(c.basic_sth)
print(a.basic_sth, a.a_sth)
print( b.b_sth)
# print(b.basic_sth) # error, because b donot call the __init__ of BaseClass

'''
<class '__main__.BaseClass'> Functions will be inherited by default
<class '__main__.A'> Functions will be inherited by default
<class '__main__.B'> Functions will be inherited by default
this function do not needs self, because it belongs to Class, not object
call it by BasicClass.sfunc()
this function do not needs self, because it belongs to Class, not object
call it by BasicClass.sfunc()
this function do not needs self, because it belongs to Class, not object
call it by BasicClass.sfunc()
this function do not needs self, because it belongs to Class, not object
call it by BasicClass.sfunc()
try to check elements
0
0 1
2
'''