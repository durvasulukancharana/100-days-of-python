# key word variable length argument:--

def fun(**v):
    print(v)
fun(name="vamsi",name2="ravi",name3="pablo",name4="charan")

def fun(**v):
    for a,b in v.items():
        print(a,b)
fun(name="vamsi",name2="ravi",name3="pablo",name4="charan")