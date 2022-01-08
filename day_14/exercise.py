from time import time


def performance(fn):
    def wrap_fun(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f'It took {t2 - t1}')
        return result

    return wrap_fun


@performance
def do_some_math():
    for i in range(10000000):
        i * 5


do_some_math()
