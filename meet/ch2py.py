#!/usr/bin/env python
# coding: utf-8

# # Chapter 2 : Condition Execution and Iteration

# write a python programe to calculate number of notes (500, 200, 100, 50, 20, 10) if we will give user input values.

# In[18]:


bill=int(input("Enter the bill amount : "))
note500= (bill//500)
print("Notes of 500 is ", note500)
bill1= (bill%500)
note200= (bill1//200)
print("Notes of 200 is", note200)


# In[22]:


#Condition 1. Simple if


# In[25]:


#condition 2. if else
name= input("Enter youre name : ")
if name== "Meet":
    print("I am Meet")
else:
        print("I am not meet")


# In[26]:


#condition 3.  if elif else 
a= int(input("Enter value a ="))
b= int(input("Enter value b ="))
c= int(input("Enter value c ="))
if a>b and a>c:
    print("a is highest number")
elif b>c:
    print("b is highest number")
else:
    print("c is highest number")


# In[34]:


# condition 4. Nested if
x=int(input("Enter the number  = "))
if x > 10:
    print("greater than 10")
    if x > 20:
        print("greater than 20")
else:
    print("Less than 10")


# # For Loop

# In[44]:


for i in range(6):
    print(i)


# In[47]:


s="Gohil Meet"
for i in s:
    print(i)


# # While Loop

# In[49]:


x=1
while x<6:
    print(x)
    x=x+1


# # Nested Loop

# In[52]:


for i in range(3):
    for j in range(3):
        print("i=",i,"j=",j)


# In[1]:


print("hello")


# In[3]:


for i in range(10):
    if i==7:
        print("Iteration is enough")
        break
    print(i)


# In[4]:


for i in range(10):
    if i==7:
        print("Iteration is enough")
        continue
    print(i)


# 2.Write a python programme to check even year is leap year or not.

# In[11]:


y=int(input("Enter Year: "))
if y%4==0 and y%100!=0 or y%400==0:
    print("Leap year")
else:
        print("Not leap year")


# 3. Write a python programme to perform arethmetic operation according to choice given by user.

# In[20]:


a=int(input("Enter A value= "))
b=int(input("Enter B value= "))
c=input("Enter Choice = ")
if c=="+":
    print("Addition is= ",a+b)
elif c=="-":
    print("Substraction is= ",a-b)
elif c=="*":
    print("Multiplication is= ",a*b)
elif c=="%":
    print("Module is= ",a%b)
elif c=="/":
    print("division is= ",a/b)
else:
    print("Enter a valid choice= ")


# 3. Write a pyhon programme 

# In[33]:


m=int(input("Enter Marks ="))
if m>80 and m<100:
    print("Distinction")
elif m>60 and m<79:
    print("First class")
elif m>35 and m<59:
    print("Second class")
    else m<35:
        print("F")


# In[43]:


c=input("Enter Character Value : ")
if c=="a" or c=="e" or c=="i"or c=="o" or c=="A" or c=="E" or c=="I"or c=="O" or c=="u" or c=="U":
    print("Character is Vovel")
else:
    print("Character is consenet")
    
    


# 5. Write a pyhton programme to calculate the electicity bill(No.of units decides by user) 

# In[49]:


unit=int(input("Enter no.of unit="))
amount=0
if unit<=100:
    print("amount to be paid=",amount)
elif unit>100 and unit<=200:
    amount=(unit-100)*5
    print("amount to be paid=",amount)
else:
    amount=500+(unit-200)*10
    print("amount to be paid=",amount)


# #. Accept the following from the user and calculate the percentage of class attendance
# a=number of workimg days
# b= total no.of days for absent
# after calculating percentage show that if percentage is >70 students are eligible for attendece bonus othewise not
# 

# In[54]:


a=int(input("Enter the number of working days="))
b=int(input("Enter the number of Not working days="))
c=a-b
per=(c/a)*100
print("percentage of attendence=",per)
if per>=70:
    print("youre eligable for attendence bonus ")
else:
    print("youre not eligable for attendence bonus ")
    


# 7. Write a pyhton programme to take the cost bike of price from user and display the road taxe to be paid based on purchase price of bike

# In[9]:


cost=int(input("Enter the purchasing price of bike="))

if cost>200000:
    tax=15*(cost/100)
    print(tax)
elif cost>=100000 and cost<=200000:
    tax=10*(cost/100)
    print(tax)
else cost<10000:
    tax=5*(cost/100)
    print(tax)
    
    


# 7.Take the age and gender, no. of days and display the wages accordingly 
# if age doesnt fall in any range than display the following reason 1.enter appropiate age

# In[ ]:


age=int(input("Enter age is="))
gender=input("Enter gender is=")
day=int(input("Enter no. of present day="))
if age>=18 and age<30 and gender=="M":
    paid=700*day
    print("Total wages is=",paid)
elif age>=18 and age<30 and gender=="F":
    paid=750*day
    print("Total wages is=",paid)
elif age>=30 and age<=40 and gender=="M":
    paid=800*day
    print("Total wages is=",paid)
elif age>=30 and age<=40 and gender=="F":
    paid=850*day
    print("Total wages is=",paid)
else:
    print("Please enter appropiate age")


# In[ ]:


#Q. write a python programme to find sum of N number

n=int(input("Enter the number = "))
sum=0
for i in range (1,n+1):
    sum=sum+i
print("Total :",sum)
print("Average", sum/n)


# 2.write a python programme to read three numbers(a,b,c) and check how many numbers between a and b which is divisable by c.

# In[13]:


a=int(input("Number A: "))
b=int(input("Number B: "))
c=int(input("Number C: "))
count=0
for i in range(a+1,b):
    if(i%c==0):
        count+=1
print("Count which is divisable by c = ",count)
    


# 3. Write pyhton programme multiplication  table of given number by user.

# In[4]:


a=int(input("Enter the number = "))
i=1
while i<=10:
    print(a,"*",i,"=",a*i)
    i+=1


# 4. Write pyhton  programme to find out factorial of given number.

# In[18]:


n=int(input("Enter the number : "))
fact=1
if n<0:
    print("!!Enter Valid Value!!")
elif n==0 and n==1:
    print("Factorial is : ",fact)
else:
    for i in range (2,n+1):
        fact=fact*i
    print("Youre factorial is : ",fact)


# 5. write a python programme to find out reverse number provided by user.

# In[33]:


n=int(input("Enter the number : "))
rev_num=0
temp=n
while n!=0:
    ld=(n%10)
    rev_num=rev_num*10+ld
    n=(n//10)
print("Reverse number is : ",rev_num)

if rev_num==temp:
    print("Its palindrone")
else:
    print("Its not palindrone")


# 6. Write a python programme to check given number is armstrong or not.

# In[35]:


n=int(input("Enter the number : "))
temp=n
sum=0
l=len(str(n))
while n!=0:
    ld=(n%10)
    sum=sum=(ld**l)
    n=(n//10)
print("Youre sum of answer",sum)

if sum==temp:
    print("Number is Armstrong")
else:
    print("Number is not Armstrong")
    


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# 7. Write a python programme to display fibonacci sequence upto Nth term

# In[42]:


n=int(input("Number a: "))
n1=0
n2=1
if n<=0:
    print("Enter the valid value")
elif n==1:
    print("Fibonacci Series:\n",n1)
else:
    print("Fibonacci Series")
    print(n1)
    print(n2)
    for i in range(0,n-2):
        nth=n1+n2
        print(nth)
        n1=n2
        n2=nth
        


# 8. Happy numebr.

# In[ ]:




