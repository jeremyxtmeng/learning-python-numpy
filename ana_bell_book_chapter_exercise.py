
# ex 17.1 
x=0
for i in range(2,102,2):
    if i%6==0:
        x+=1
print("even numbers divsible by 6 is", x)

# ex 17.2
n=4
for i in range(n,0,-1):
  print(i, "books on Python on the shelf", i, "books on Python")
  print("Take one down, pass it around,", i-1, "books left.")

# ex 17.3
x="Zoe Xander Young"
k=""
for i in x+" ": # adding " " for stopping
    if i!=" ":
        k=k+i
    else:
        print("Hi", k)
        k=""

# ex 18.1
num = 8
guess = int(input("Guess my number: "))
while guess != num:
    guess = int(input("Guess again: "))
print("Right!")

# ex 18.2
if input("you want a game")=="y":
    guess=int(input("guess a number"))
    while guess!=10:
        guess=int(input("guess a number"))
    print("You guessed the right number")

# ex 22.1
def area(shape, n):
    return shape(n)
def circle(radius):
    return 3.14*radius**2
def square(length):
    return length*length

print(area(circle, 5))

# ex 22.2
def person(age):
    print("I am a person")
    def student(major):
        print("I like learning")
        def vacation(place):
            print("But I need to take breaks")
            print(age,"|",major,"|",place)
        return vacation
    return student
person(12)("Math")("beach")

# ex 25.1
menu = []
food=["pizza", "beer", "fries", "wings", "salad"]
menu.extend(food)
menu.pop(menu.index("beer"))
menu.pop(0)
menu[0]="quinoa"
menu[1]="steak"

# ex ch 25.2
def unique(list_orig):
    # L=list_orig      create a reference to the original list
    # code below also modify the original list
    L=list_orig.copy()
    LL=[]
    LL.append(L.pop())
    while len(L)>0:
        if LL.count(L[-1])==0:
            LL.append(L.pop())
        else:
            L.pop()
    return LL

def unique2(list_orig):
    L=[]
    for n in list_orig:
        if n not in L:
            L.append(n)
    return L

AA=[1, 2, 4 , 5, 2, 7]
unique2(AA)
    
# ex ch 25.3
def check_common(LL1, LL2):
    size1=len(LL1)
    while len(LL2)>0:
        LL1.append(LL2.pop())
        if len(unique(LL1))==5:
            check=0
            continue
        else:
            check=1
            break
    return check

check_common([7, 2, 5, 4, 1], [7, 40,1])


# can use numbers to replace true or false in the if statement
# Python treats None, 0, "", [], {} as false → not false → True
a=1
if a: 
    print("true")
else:
    print("false")


LL1=[7, 2, 5, 4, 1]
LL2=[7, 4,1]

def common(L1, L2):
    LL1=unique(L1)
    LL2=unique(L2)
    if check_common(L1, L2) and check_common(L2, L1):
        print("True")
    else:
        print("False")

common(LL1, LL2)

# ex ch 26
cities = "san francisco,boston,chicago,indianapolis"
L=cities.split(",")
L.sort()
print(L)

# ex ch 26
def is_permutation(L1, L2):
    a1=unique2(L1)
    a2=unique2(L2)
    a1.sort()
    a2.sort()

    if len(L1) != len(L2):
        check=0
    elif a1 != a2:
        check=0
    else:
        for i in L1:
            if L1.count(i) != L2.count(i):
                check=0
                break
            else:
                check=1
        for i in L2:
            if L1.count(i) != L2.count(i):
                check=0
                break
            else:
                check=1
    return check

def is_permutation2(L1, L2):
    L1.sort()
    L2.sort()
    return L1 == L2

is_permutation([1,2,3], [3,1,2])
is_permutation([1,1,1,2], [1,2,1,1])
is_permutation([1,2,3,1], [1,2,3])
is_permutation([1,2,3,1], [1,2,3,3])
            

# ex ch 27
household = {"person":4, "worm": 2, "cat":2, "dog":1, "fish":2}
for i in household:
    print(i)

for i in household.keys():
    if household[i]==2:
        print(i)
# ex ch 27
def replace(d,v,e):
    for i in d:
        if d[i]==v:
            d[i]=e
    return d
replace({1:2, 3:4, 4:2}, 2, 7)

replace({1:2, 3:1, 4:2}, 1, 2)

# ex ch 27
def invert(d):
    for i in d:
        k=d[i]
        d.pop(i)
        d[k]=[i]
    return d

invert({1:2, 3:4, 5:6})        

# ex ch 28
d={1: 2, 2:3, 4: 5}

def invert_dict(d):
    d2={}
    for i in d:
        k=d[i]
        d2[k]=i
    return d2
invert_dict(d)

d={1: 2, 2:3, 4: 5}
def invert_dict_inplace(d):
    for old_key in list(d.keys()):        # list() to avoid RuntimeError
        value = d.pop(old_key)            # remove old key, get its value
        d[value] = old_key

d={1: 2, 2:3, 4: 5}

def invert_dict_inplace2(d):
    items = list(d.items())
    d.clear()
    for k, v in items:
        d[v] = k
invert_dict_inplace2(d)
print(d)

# ex 31.1
class Door(object):
    def __init__(self):
        self.width = 1.2
        self.height = 2
        self.open = False
    def opendoor(self):
        self.open=True
    def cwidth(self,width):
        self.width=width
    def cheight(self,height):
        self.height=height
    def get_area(self):
        return self.width *self.height

a=Door()
a.cheight(2)
a.cwidth(3)
a.get_area()

# Use dot for class
class Rectangle(object):
    """ a rectangle object with a length and a width """
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def set_length(self, length):
        self.length = length
    def set_width(self, width):
        self.width = width

a=Rectangle()
a = Rectangle(1,1)
a.set_length(4) # two ways are identical
Rectangle.set_length(a,4)

# ex ch 31
class Circle(object):
    """Write a method for the circle class named get_area"""
    def __init__(self):
        self.radius=0
    def change_radius(self,r):
        self.radius=r
    def get_area(self):
        return 3.14*(self.radius**2)
    
c=Circle()
Circle.change_radius(c,2)
c.get_area()

