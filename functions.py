


from unicodedata import name


def hello():
    print("Hello Adalab")

def hello(name,age):
    year=2022-age
    print(f"hello {name} you were born in {year}")

def hello2(name):
        print(f"hello {name}")
        return
        print("welcome to Adalab")

def hello3(name):
        return f"Hello{name}"

def my_country(name,country="uganda"):
    return f"hello{name} from country"

def hello_multi(*names):
    for name in names:
      print(f"hello {name}")

def sum(*number):
    sum=0
    for num in number:
        sum+=number
    return sum
def greet_multiple(**kwargs):
    keys=kwargs.keys
    if "name" in keys:
      print("hello {kwargs['name']}")

    elif "country" in keys:
        print("hello from {kwargs[country]}")
    else:
            print("hello")
def sum_and_greet(*args,**kwargs):
    print(args)
    print(kwargs)

# def sum_and_greet(*args,**kwargs):
#     print(args)
#     print(kwargs)

def multiples_and_greet(*numbers,**student):
    num=1
    for y in numbers:
       num*=y
       print (num)
    print (f"Hello {student}")


