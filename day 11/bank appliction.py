# ***bank form using oops***

import random
class bank:
    holder_detail=[]
    def create_account(self):

        new_holder={}
        name=input("enter name:")
        if name.isalpha():
            if name[0].isupper():
                new_holder["holder_name"]=name
            else:
                print("first letter is capital")
        else:
            print("invalid name please enter your name correctly") 
        mobile_num=input("enter mobile num:")
        if len(mobile_num)==10:
            new_holder["mobile num"]=mobile_num
        else:
            print("enter valid num")
            
        aadhar_num=input("enter aadhar num:")
        if len(aadhar_num)==12:
            new_holder["holder_aadhar"]=aadhar_num
        else:
            print("valid aadhar number")
        new_holder["IFSC"]="IFSC01256"
        data=random.randint(1000000000,9999999999)
        new_holder["account_num"]=data
        n=input("type of account saving/zero:")
        if n=="saving":
            while True:
                n1=int(input("your account is saving.so you have to deposite 500 rupees:"))
                if n1>=500:
                    new_holder["balance"]=n1
                    break
                else:
                    print("deposite 500 rupees")
        if n=="zero":
            while True:
                n2=int(input("your account is zero.so you have to deposite 100:"))
                if n2>=100:
                    new_holder["balance"]=n2
                    break
                else:
                    print("deposite 100")
        bank.holder_detail.append(new_holder)
        print(bank.holder_detail)

obj=bank()
obj.create_account()