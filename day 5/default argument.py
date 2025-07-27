# default argument:--

def fun(name="teja",age=20):
    print("name",name)
    print("age",age)
fun()

def fun(name="teja",age=20):
    print("name",name)
    print("age",age)
fun(name="pablo")

def fun(name="teja",age=20):
    print("name",name)
    print("age",age)
fun(name="pablo",age=25)

def fun(c,a=10,b=20):
    print("a:-",a)
    print("b:-",b)
    print("c:-",c)
fun(10,20,30)

def fun(c,a=10,b=20):
    print("a:-",a)
    print("b:-",b)
    print("c:-",c)
fun(c=10,a=60,b=90)