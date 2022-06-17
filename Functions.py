# def                     --> Function Keyword [Define]
# say_hello()             --> Function Name
# name                    --> Parameter
# print(f"Hello {name}")  --> Task
# say_hello("Ahmed")      --> Ahmed is The Argument

def say_hello(name):

  print(f"Hello {name}")

say_hello("Ahmed")


# parameters
'''
    - required
    - keyword
    - default
    - variable length
'''

# required

def mysum(x,y):
    return(x+y)


s = mysum(3,6)
print(s)

 
# keyword

def keyword(x,y):
    return x+y

b = keyword(x=15,y=9)
print(b)

# defaulr

def default(x=0,y=0):
    return x+y

z = default()
print(z)


# anonymous function

anon = lambda x,y : x+y
print(anon(45,88))


(lambda x,y : x+y)(10,15)



# Scope = local & global

f = 0
print(f)       #-----> global

def do():
    global f   #----> to make f global
    f = 5      #----> local
    print(f)

do()
print(f)









