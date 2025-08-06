# basic math and logic paper:--1

# 1. Area of Square
input=5
# area of square=side*side
print(input*input)

# 2. Area of Rectangle
length=10
breadth=20
i=length*breadth
print("Area of Rectangle",i)

# 3. Area of Triangle
base=8
height=5
form=((1/2)*base*height)
print("Area of Triangle",form)

# 4. Perimeter of Square
side=6
perimeter=4*side
print("Perimeter of Square",perimeter)

# 5. Perimeter of Rectangle
length=5
breadth=3
perimeter=(2*(length+breadth))
print("Perimeter of Rectangle",perimeter)

# 6. Perimeter of Triangle
a=5
b=6
c=7
perimeter=(a+b+c)
print("Perimeter of Triangle",perimeter)

# 7. Break Amount into 1000s, 500s, and Remaining Change
amount=3700
note1000= amount//1000
print(note1000)
remaining=amount-(amount//1000)*1000
print(remaining)
note500=remaining//500
print(note500)
remaining=remaining-(remaining//500)*500
print(remaining)

amount=5931
note1000=amount//1000
print("1000 notes are",note1000)
remain=amount-(note1000*1000)
print(remain)
note500=remain//500
print("500 notes are",note500)
remain=remain-(note500*500)
print(remain)
note200=remain//200
print("200 notes are",note200)
remain=remain-(note200*200)
print(remain)
note10=remain//10
print("10 notes are",note10)
remain=remain-(note10*10)
print(remain)
note1=remain//1
print("1 note is",note1)
remain=remain-(note1*1)
print(remain)

# 8. Convert Seconds into Hours, Minutes, and Seconds
totalsec=3672
hours=totalsec//(60*60)
print("hours",hours)
remain=totalsec-hours*(60*60)
print(remain)
min=remain//60
print('min',min)
remain=remain-min*60
print(remain)
sec=remain//60
print('sec',sec)

totalsec=4000
hours=totalsec//(60*60)
print(hours)
remain=totalsec-hours*(60*60)
print(remain)
min=remain//60
print(min)
remain=remain-min*60
print(remain)
sec=remain//60
print(sec)

# 9. Sum of Marks (Maths, Physics, Chemistry)
math=85
phy=90
che=88
print(math+phy+che)

a=85
b=90
c=88
print((a+b+c)/3)