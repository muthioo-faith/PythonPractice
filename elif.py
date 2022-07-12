# x=range(30)
# for y in x:
#     if y%4==0:
#         print(f"{y} is divisible by 4")
#     elif y%7==0:
#         print(f"{y} is divisible by 5")
#     elif y%7==0:
#         print(f"{y} is divisible by 5")
#     else:
#         print(f"{y} is not divisible by 4,5 or 7")
# f="tomorrow"
# g=""
# for i in f:
#     if i not in g:
#         g+=i
# print(g)

# f=[1,2,3,1,2,4,5,6]
# g=[]
# for i in f:
#     if i not in g:
#         g.append(i)
# print(g)

# numbers=[1,2,3,4]
# numbers[0],numbers[-1]=numbers[-1],numbers[0]
# print(numbers)
# reverse
# def word(x):
#     y=x.split()
#     start=0
#     end=len(y)-1
#     while start<end:
#         y[start],y[end]=y[end],y[start]
#         start+=1
#         end-=1
#         z=" "
#     print(z.join(y))
# word("I am faith Mutua a student at AkiraChix")


 


def names(name):
    if name==name[::-1]:
        print("palindrome")
    else:
        print("not palindrome") 

names("mum") 