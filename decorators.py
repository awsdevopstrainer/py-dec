# decorators


def my_decorator(myfunc):
    def wrapper():
        print("===========================")
        myfunc()
        print("===========================")
    return wrapper

@my_decorator
def greetings():
    print("Welcome to Python Batch")
    print("This is a simple decorator example")

greetings()

# greetings()
@my_decorator
def newyear_greets():
    print("Wishing you happy new year")

newyear_greets()
# greetings()
