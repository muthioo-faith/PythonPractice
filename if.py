# x=range(20)
# for y in x:
#     if y%3==0:
#      print(y)
# ascending
def arrange():
    details={"moses":48,"Hilda":10,"laura":27}
    details2=list(details.items())
    # details2=list(details.keys())
    details2.sort()
    print(dict(details2))
      
arrange()

def names(name):
    if name==name[::1]:
        print("palindrome")
    else:
        print("not palindrome") 

names("mum") 


numbers=[2,3,4,5,6,7]
[0],[-1]
numbers[0],numbers[-1]=numbers[-1],numbers[0]
print(numbers)  