# Decorators Pattern
def my_decorator(function):
    def wrap_func(*args, **kwargs):
        print("*************")
        function(*args, **kwargs)
        print("*************")
    return wrap_func


@my_decorator
def hello(fname='MR.', lname='boss'):
    print(f"Helllloooo {fname} {lname} Keep going, you are best, I know")


hello('MR.', 'Sakhawat')
