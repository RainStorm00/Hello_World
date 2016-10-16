a = 7823

def corn():
    #if a varaiable is created inside of a function, only the function can use it.
    print(a)

def fudge():
    print(a)

corn()
fudge()