# def factorial():
#     y = 5
#     fact=1
#     for x in range(1,y+1):
#         fact*=x
#     return fact
# print (factorial() )       
        
# from sys import flags


# def fruits(x):
#  x = [2,3,4,5,6,7,8]
#  return x[2:-1]
# flavor = fruits('apple')

# print(flavor)

# def letters(y):
#     letters=["1","2","3","4"]
# num=reversed(letters)
# for x in num:
#       print(num)

# alph = [1, 2, 3, 4]

# ralph = reversed(alph)
# for x in ralph:
#    print(x)  
# i = 1
# while i > 6:
#   print(i)
#   i -= 1 
# from itertools import count


# from itertools import count

# v = 0
# for x in range(100):
#   if x%7==0:
#     print(x,end="")

#     v = v +1

#     if v == 9:
#         break



# from operator import index


# x=[2,3,4,5,6,7,8]  
# for index, i in enumerate(x):
#     x[index]=i*i
#     print(x)
    
# x=[23,4,-6,23,-9,21,3,-45,8]
# pos=[]
# neg = []
# for i in range(len(x)):
#     if x[i]<0:
#         neg.append(x[i])

#     else:
#         pos.append(x[i])

# print(pos)
# print(neg)
        
# for i in range(1,10):
#     if i%2==0:
#         print("even", i)
#     else:
#         print("old" , i)
            
            
# dic={"val1":10,"val2":20,"val3":23,"val4":22}  
# for y in dic.values():
#     if y %2 == 0:
#         print(y) 
#     else:
#         pass
# a="winnie"
# count=0
# for i in a:
#     count+=1

#     print(count)

# b="winnie"
# x = b.replace("i","a")
# print(x)
# a="i love school"
# # x="love" in a
# print ("orage" in a.split())

# f="Faith mutua mwende"
# g=f[0],f[6],f[12:18]
# print(g)

# f="Hello Faith Mutua "
# a=['a','e','i','o','u','A','E','I','O','U']
# for i in f:
#  if  i not in  a:
#      f=f[:f.index(i)]+f[f.index(i)+1:]
# print(f)

# # Given the list a = [150, 250, 350, 450, 550], use a list comprehension 
# # to create a new list b where each number in a is divided by 9



# a = [150, 250, 350, 450, 550]
# b=[b/9 for b in a]
# print(b)


# # Given the tuple y = (10,20,30,40,50), on you interpreter use a for 
# # loop to print the remainder of each number divided by 3
# y=(10,20,30,40,50)

# for x in y:
#     print(x%3)

# swapping
import numbers


# listx=[1,2,3]
# listx[0],listx[-2]=listx[-2],listx[0]
# print (listx)
# consonants and vowels
# a=['a','b','c','d','e','i','o']
# for i in a:
#     print("vowels")
# else:
#     print("consonants")    


# def vowels_cons(name):
#     listv=['a','e','i','o','u']    
#     vowels=0
#     cons=0
#     for x in name:
#         if x in listv:
#           vowels+=1
#         else:
#          cons+=1

#     print(f"The number of vowels is {vowels}" )
#     print(f"The number of consonants is {cons}")

# vowels_cons("Faith")            

# t= tuple("gat","fay")
# print(t[1])

# t1 =("Python", "C++", "Java")
# # print(t[1])
# t2= ("amin", " fay")
# t3=t1+t2
# print(t3)
# # print(t[1])
# t=(1,3,4)
# print(t[::-1])

# if 'bar' in{'foo':1,'bar':2,'baz':3}:
#     print(1)
#     print(2)
#     if 'a' in 'quz':
#         print(3)
# print(4)
a=100
b=50
if a>b:
    m=b
    print(m)
else:
    m=a
    print(m)     
    