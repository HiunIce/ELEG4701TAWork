def fun1():
    print("the first funcntion")
    for i in range(3):
        print('iteration', i)
        if i == 1:
            print("print extra stuffs")
        if i == 3:
            print("it will never happens because range stops in 3")

def fun2(sth):
    print('the second funcion, input args is', sth)

def fun3(*args, **kargs):
    # you don't need to write all args
    # you can use *args and **kargs to hide them
    print(args)
    if 'kw' in kargs:
        print("has key arg kw:",kargs['kw'])
    else:
        print("other kw:", kargs)

def fun4():
    return 4

def fun5(functor):
    print(functor())

def fun():
    fun1()
    fun2('abcd')
    fun3(1, 2, 3, 4, 5, kw=6)
    #in this case, the input is a number, becase the fun4 is called before being a argument
    fun3(fun4())
    # in this case, the input is a function
    fun5(fun4)

fun() # call function here