def countdown(i):
    print(i)
    if i <= 1:
        return 0
    else:
        countdown(i-1)

#call stack
def greet(name):
    print("Hello, " + name + "!")
    greet2(name)
    print("getting ready to say bye")
    bye()

def greet2(name):
    print("How are you, " + name + "?")

def bye():
    print("ok bye!")

#recusrsion call stack
def fact(x):
    
    if x == 1:
        return 1
    else:
        return x * fact(x-1)
    
print(fact(3))
