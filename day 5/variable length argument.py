# variable length argument:--

def fun(*v):
    a=5
    print(sum(v))
fun(10,20,30)

def fun(*v):
    print(v)
fun("vamsi",26,"trainer","married")