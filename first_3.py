def new_decorator(original_func):

    def wrap_func():
        print("This is a function before the original function")
    
        original_func()

        print("This is a function after the original function")

    return wrap_func

def func_needs_decorator():
    print("I want to be decorated!!")

print(func_needs_decorator())

decorated_func = new_decorator(func_needs_decorator)

print(decorated_func())
@new_decorator
def func_needs_decorator():
    print("I want to be decorated!!")