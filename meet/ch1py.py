#!/usr/bin/env python
# coding: utf-8

# # Identifiers

# A name in python program is called identifires. 

# The identifires can be function name, variable name, class name , module name
# 

# For example X=10 , Def addition , class bus etc.
# 
# 
# 

# They only have allow character like (a-z, A-Z , 0-9 , _).

# identifires are case sensitive.

# we cannot use reserve word s identifires

# there is no length limit for python identifires

# if identifires start with _ then it indicates as private identifires

# if identifires start with _ _ then it indicates as strongely private identifires

# if identifires start with _ _ _ then it indicates as magic method.

# must start with alphabates not a digit.

# # Data types: 1. Text type
# 

# 1. Text type : str() 
#     Ex : 1. s1 = "Hello world" # Hello world 
#          2. s2 = ""Hello
#             world"" # Hello
#                      world

# # 2. Numerical data type : 1. integer , 2. float , 3. complex
#    

# In[7]:


# 1.integer datatype
x=1
y=12345
z=-123
print(type(x))
print(type(y))
print(type(z))


# In[12]:


# 2.float datatype
x=1.3
y=12345.45
z=-123.567
print(type(x))
print(type(y))
print(type(z))


# In[11]:


i=3.6e4
print(i)
print(type(i))


# In[16]:


# 3.complex datatype
x= 3+4j
y= -3-4j
print(y)
print(type(y))


# # 3. Sequence data type : 1.list() , 2. tuple() , 3. range()

# In[21]:


# 1. list() order , changebal , allow dupliacte
l1 = ['ramesh' , 'bhumit', 'kabira']
print(l1)
l1[0]='meet'
print(l1)
l2= [1 ,4.5 , 'Meet']
print(l2)
print(type(l2))


# In[28]:


#2. tuple()  allow dupliacte , unchangebal , order 
t1= ('ramesh' , 'bhumit', 'kabira' , 'kabira')
print(t1)
t2 = (1 ,4.5 , 'Meet')
print(t2)
print(type(t2))


# In[33]:


# 3. range() 
x= range(4)

print(x)
print(type(x))


# # 4. Mapping type: dict()

# In[36]:


#dictionary not allowed duplicate key , ordered, 
d={1:'meet', 2:'bhumit', 3:40 , 4:40}
print(d)
print(type(d))
print(d[2])


# # 5. Set Data Type

# In[45]:


# 1. set() unorder , Not allowed duplicate value , unchangable
s= {12, 23 ,45, 67, 67, 9}
print(s)
print(type(s))


# In[55]:


t= (10,20,30,40,50)
print(t)


# In[52]:


l=[10,20,30,40,50]
print(l)
l.remove(40)
print(l)


# In[53]:


s={12, 23 ,45, 67, 67, 9}
print(s)


# In[57]:


# 2. frozen set()
fs={12, 23 ,45, 67, 67, 9}
print(frozenset(fs))
print(type(fs))


# # 6. Boolean type 

# In[60]:


# Bool type 
x= True
print(x)
print(type(x))


# In[61]:


# Logic of Boolean
print(bool(0))
print(bool(1234))
print(bool(""))
print(bool("  "))


# # Type casting 1. int

# In[75]:


print(int(10))
print(int(14.99))
print(int(188.59))
print(int("99"))
print(int(67.89))
#print(int("23.23"))
print(int(7.5))


# # 2. Float()

# In[82]:


print(float(10))
print(float(14.99))
print(float(188.59))
print(float("99"))
print(float(67.89))
print(float("23.23"))
print(float(7.5))
#print(float("ten"))
print(float("123"))


# # 3. Bool

# In[83]:


print(bool(0))
print(bool(123))
print(bool(0.0))
print(bool(1.23))
print(bool("False"))
print(bool(""))
print(bool(0+0j))
print(bool(0+4j))


# # 4. str( )

# In[5]:


str(10)
str(10.4)
#str(10+4j)


# In[7]:


str(True)
str(False)


# # 5. Variable

# x=10 v
# _x=10 v 
# _x_=10 nv
# 123x='ramesh' nv
# x123='ramesh' v
# 

# In[14]:


a,b,c,d = 10,20,30,40
print(a,b,c,d)


# In[17]:


a=b=c="apple"
print(a)
print(b)
print(c)


# In[29]:


a=input("Enter you're name: ")
#print("My name is :" +a)
#print("My name is :" ,a)
print(f"My name is : {a}")


# # Operators

# 1. Arithmetic operator
# 

# In[ ]:


a=10
b=3
print(a+b)
print(a-b)
print(a/b)
print(a*b)
print(a//b)
print(a%b)
print(a**b)


# In[ ]:


x= "arman"
print(x*5)


# 2. Relational Operator / comparison operator

# In[10]:


a=10
b=10
print(a>b)
print(a<b)
print(a==b)
print(a<=b)
print(a>=b)
print(a!=b)


# In[11]:


print(10<20<30<=35)
print(10<20<30<40)
print(10<=10<20<=30<40)
print(10<20<30<40>50)


# In[40]:


# For the string 
"Arman">"Meet"


# In[49]:


chr(65)


#  3.Ternary Operator

# In[52]:



a=40
b=30
x=30 if a>b else 40
print(x)


# 4. Logical Operators

# In[53]:


True and False


# In[54]:


True or False


# In[59]:


not True


# In[60]:


# Non boolean type 
10 and 0 


# In[61]:


0 and 10


# In[63]:


"arman" and 9


# In[66]:


print(10 or 0) 
print(0 or 10)
"arman" or 9


# 5. Membership Operator

# In[79]:


l=[10,20,30,40,50]
print(80 in l)
s="Hello python is very easy"
print("H" in s)
t=(12,34,56,78)
print( 2 not in t)


# 6. Assignment Operatore

# In[92]:





# In[ ]:




