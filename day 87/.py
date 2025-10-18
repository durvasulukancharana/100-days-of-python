'''inheritance'''
# Inheritance allows a class (child) to acquire properties and methods of another class (parent).
# Promotes code reusability and modularity.
# Types: Single, Multiple, Multilevel, Hierarchical, Hybrid.


'''single inheritance'''
# One child inherits from one parent.

# class person:
#     def __init__(self,name):
#         self.name=name
#     def greet(self):
#         print(f'hello {self.name}')

# class employee(person):
#     def __init__(self,name,emp_id):
#         super().__init__(name)
#         self.emp_id=emp_id
#     def show_details(self):
#         print(f'hii {self.name} and your id is {self.emp_id}')

# x=employee('vamsi',101)
# x.greet()
# x.show_details()


# class person:
#     def det(self,name):
#         self.name=name
#     def greet(self):
#         print(f'hello {self.name}')

# class employee(person):
#     def ted(self,name,emp_id):
#         super().det(name)
#         self.emp_id=emp_id
#     def show_details(self):
#         print(f'hii {self.name} and your id is {self.emp_id}')

# x=employee()
# x.ted('vamsi',101)
# x.greet()
# x.show_details()


'''multiple inheritance'''
# Child inherits from more than one parent.

# class person:
#     def greet(self):
#         print('hello world')
    
# class company:
#     def info(self):
#         print('this is a company')

# class employee(person,company):
#     def work(self):
#         return ('this is employee')

# obj=employee()
# obj.greet()
# obj.info()
# print(obj.work())


'''multilevel inheritnce'''
# Inheritance chain: Parent → Child → Grandchild

# class person:
#     def greet(self):
#         print('this is person')

# class employee(person):
#     def work(self):
#         print('this is employe')

# class manger(employee):
#     def manage(self):
#         print('this is manager')

# obj=manger()
# obj.greet()
# obj.work()
# obj.manage()


'''hierachicle inheritance'''
# Multiple children inherit from one parent

# class parent:
#     def greet(self):
#         print('this is parent')

# class child1(parent):
#     def work(self):
#         print('this is child 1')

# class child2(parent):
#     def study(self):
#         print('this is child 2')

# x=child1()
# x.greet()
# x.work()
# y=child2()
# y.greet()
# y.study()



'''hybrid inheritance'''
# Combination of multiple types (Single, Multiple, Multilevel, Hierarchical)

# class grand_parent:
#     def name(self):
#         print('hello')

# class parent:
#     def age(self):
#         print('this is parent')

# class child(grand_parent,parent):
#     def son(self):
#         print('this is child')

# class grand_child(child):
#     def child(self):
#         print('grand child')

# obj=grand_child()
# obj.name()
# obj.age()
# obj.son()
# obj.child()



'''super function'''

# class parent():
#     def age(self,name):
#         self.name=name
#         print(self.name)
    
# class child(parent):
#     def name(self,name,age):
#         super().age(name)
#         self.age=age
#         print(self.age)
# obj=child()
# obj.name('ajay',23)



'''school management system'''

# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#         print(f'hello {self.name} and your age is {self.age}')
# class student(person):
#     def __init__(self,name,age,grade):
#         super().__init__(name,age)
#         self.grade=grade
#         print(f'hello {self.name} your grade is {self.grade}')
# class teacher(person):
#     def __init__(self,name,age,subject):
#         super().__init__(name,age)
#         self.subject=subject
#         print(f'hello {self.name} your subject is {self.subject}')

# x=student('vamsi',29,'A+')
# # print(x.name,x.age,x.grade)
# y=teacher('vamsi',29,'python')
# # print(y.age,y.name,y.subject)



'''banking system'''

# class account:
#     def __init__(self,owner,balance):
#         self.owner=owner
#         self.balance=balance

# class savings(account):
#     def deposite(self,amount):
#         self.balance+=amount
#         print(f'{amount} deposited so your balance is {self.balance}')

# class current(account):
#     def withdraw(self,amount):
#         if amount<=self.balance:
#             self.balance-=amount
#             print(f'{amount} withdraw so your balance is {self.balance}')
#         else:
#             print('insufficient balance')

# x=savings('vamsi',1000)
# x.deposite(200)

# y=current('ajay',1000)
# y.withdraw(500)



'''E-commerce user system'''
# class user:
#     def __init__(self,name):
#         self.name=name

# class customer(user):
#     def place_holder(self,item):
#         self.item=item
#         print(f'{self.name} added {self.item}')

# class seller(user):
#     def add_product(self,product):
#         print(f'{self.name} added {product} for sale')

# x=customer('ajay')
# x.place_holder('laptop')
# y=seller('vamsi')
# y.add_product('royal enfield')



'''hospital management'''

# class person:
#     def name(self,name):
#         self.name=name

# class patient(person):
#     def medicine(self,med,name):
#         super().name(name)
#         print(f'{self.name} takes {med}')

# class doc(person):
#     def prescri(self,med,name):
#         super().name(name)
#         print(f'{self.name} prescribe {med}')

# z=person()
# z.name('ajay')
# x=patient()
# x.medicine('ajay','dolo')
# y=doc()
# y.prescri('ajay','vamsi')



# class person:
#     def __init__(self,name):
#         self.name=name

# class patient(person):
#     def medicine(self,med):
#         # super().name(name)
#         print(f'{self.name} takes {med}')

# class doc(person):
#     def prescri(self,med):
#         # super().name(name)
#         print(f'{self.name} prescribe {med}')

# x=patient('ajay')
# x.medicine('dolo')
# y=doc('vamsi')
# y.prescri('antibiotic')



'''online course platform'''

# class user:
#     def __init__(self,username):
#         self.username=username

# class student(user):
#     def enroll(self,course):
#         print(f'{self.username} enrolled in {course}')

# class instructor(user):
#     def create_course(self,course):
#         print(f'{self.username} created course {course}')

# x=student('vamsi')
# x.enroll('trainer')
# y=instructor('ajay')
# y.create_course('python')
