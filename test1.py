def string(func):
    def wrapper(*args):
        t = func(args[0])
        print(t)
        print(t)
    return wrapper


@string
def function(txt):
    return txt + '!'


function('Hi')
