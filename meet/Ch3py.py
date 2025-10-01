#!/usr/bin/env python
# coding: utf-8

# # Chapter - 3  Function & Scoping

# # Different category for user defined function

# In[4]:



def wish():
    name=input("Enter youer name : ")
    print(name)
wish()


# 1.Function withoute parameter and no return type
# 

# In[12]:



def wish():
    name=input("Enter youer name : ")
    print(name)
wish()


# 2.Function with parameter and no return type

# In[14]:


name=input("Enter youer name : ")
def wish(name):
    print(name)
wish(name)


# 3.Function without parameter and with return type

# In[16]:


def run():
    name=input("Enter the name : ")
    return name
    
run()


# 4. Function with parameter with return type

# In[18]:



def run(name):
    
    return name
name=input("Enter the name : ")    
run(name)


# In[20]:


name=input("Enter the name : ")    
def run(name):
    return name 
run(name)


# In[22]:


def wish(name):
    print("Hello",name,"Good Morning")
wish("Meet")
wish("Bhumit")
wish("Maulilk")


# In[25]:


n=int(input("Enter any Number : "))
def check(n):
    if n%2==0:
        print("even")
    else:
        print("Odd")
check(n)


# In[31]:


def add(a,b):
    return a+b
print(add(10,20))
print(add(5,20))
print(add(1,20))


# In[2]:


def cal(a,b):
    add=a+b
    sub=a-b
    mul=a*b
    return add,sub,mul

a,b,c = cal(10,20)
print(a)
print(b)
print(c)


# In[1]:


s={10,20,30,40}
s.add(50)
print(s)


# In[8]:


def add(a,b):
   
    """This function is used for Addition
        a(int):a is first
        b(int):b is second"""
    return a+b
print(add(10,5))
print(add.__doc__)


# # Types of Arguments

# 1. Positional argument
# 2. Keyword argument
# 3. Default argument
# 4. Variable length argument

# In[12]:


# 1 . Posotional Arguments
def sub(a,b):
    return a+b
print(sub(10,20))
print(sub(20,1))


# In[2]:


# 2. Keyword Arguments
def wish(name,msg):
    print("Hello",name,msg)
wish(name="Meet",msg="Good morning")
wish("Meet",msg="good morning")
wish("Meet","Good morning")
wish(msg="Good morning",name="Meet")


# In[6]:


# 3. Default Arguments
def wish(name="Meet"):
    print("Hello",name,"How are you")
wish()
wish("Bhumit")


# In[6]:


# 4. Variable length Arguments
def sum(*s):
    total=0
    for i in s:
        total=total+i
    print(total)
sum(10)
sum(10,20,30,40)
sum(10,20,30,40,50,60)
print()
def sum(n1,*s):
    total=0
    for i in s:
        total=total+i
    print(total)
print()
sum(10)
sum(10,20,30,40)
sum(10,20,30,40,50,60)


# In[17]:


def sum(*s,n1):
    total=0
    for i in s:
        total=total+i
    print(total)

sum(10,20,30,40,n1=56)


# In[19]:


x=3 # global
def fun(a):
    x=5 # local
    return x*a
print(fun(5))
print(x) # global


# In[21]:


x=3 # global
def fun(a):
    global x # local to new global
    x=5
    return x*a
print(fun(5))
print(x)


# # Nested Function

# In[28]:


def fun1():
    print("This is outer function")
    def fun2():
        print("This is inner function")
    fun2()
fun1()


# In[30]:


def fun1():
    print("This is outer function")
    def fun2():
        print("This is inner function")
    return fun2()
fun1()


# In[32]:


def fun1():
    print("This is outer function")
    def fun2():
        print("This is inner function")
fun2()


# # For else, While else

# In[34]:


for i in range(6):
    print(i)
else:
    print("Moj Ma")


# In[36]:


x=1
while x<=6:
    print(x)
    x+=1
else:
    print("Moj Moj Moj")


# In[38]:


for i in range(6):
    print(i)
    if i==3:
        break
else:
    print("Moj Ma")


# In[46]:


x=8
while x<=6:
    print(x)
    x+=1
else:
    print("Moj Moj Moj")


# In[49]:


x=1
while x<=6:
    print(x)
    x+=1
    if x==3:
        break
else:
    print("Moj Moj Moj")


# In[2]:



def armstrong(n):
    temp=n
    sum=0
    l=len(str(n))
    while n!=0:
        ld=(n%10)
        sum=sum+(ld**l)
        n=(n//10)
print("Youre sum of answer",sum)

if sum==temp:
    print("Number is Armstrong")
else:
    print("Number is not Armstrong")


# In[ ]:




