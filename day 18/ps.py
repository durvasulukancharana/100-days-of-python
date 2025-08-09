

class student:
    def __init__(self,name):
        self.name=name
        print("ading new student")
s1=student("karan")
print(s1.name)
 
class student:
    name="karan"
    def __init__(self):
        print(self)
        print("ading new student")
s1=student()
print(s1)

class student:
    # name="karan"
    # name2="arjun"
    def __init__(self,fullname,marks):
        self.name=fullname
        self.marks=marks
        print("ading new student")
s1=student("karan",19)
print(s1.name,s1.marks)
s2=student("arjun",20)
print(s2.name,s2.marks)

class student():
    
    def __init__(self,n,a,b):
        self.name=n
        self.age=a
        self.branch=b
        print(n,34)
    
kd=student("ravi",21,"ece")
print(kd.name,kd.age,kd.branch)
print(kd.age)
print(kd.branch)

class student():
    name="vamsi"
    print(name)
abc=student()
print(abc.name)

class student():
    name="vamsi"
    print(name)
    def __init__(self,name,age,branch):
        self.name=name
        self.age=age
        self.branch=branch
        print(name)
        
abc=student("ravi",21,"ECE")
print(abc.name,abc.age,abc.branch)

class student:
    name="vamsi"
    print(name)
    def __init__(self,n,a,s):
        self.name=n
        self.age=a
        self.strem=s
        print(s)
        
    def detail(self):
        print(self.name)

abc=student("ravi",21,"ECE")
abc.detail()
print(abc.strem)
print(abc.detail())

class student:
    name="vamsi"
    
    def __init__(self,n,a,s):
        year=4
        print(year,"year")
        self.name=n
        self.age=a
        self.streem=s
        print(self.name)
        print(student.name)
        student.name=n
        print(n)
        
    def detail(self):
        print(self.age)
    
    @classmethod
    def namechange(cls,newname):
        cls.name=newname
        print(cls.name,"25 line")

abc=student("ravi",20,"ece")
print(abc,"99 line")
abc.detail()
abc.namechange("rahul")

