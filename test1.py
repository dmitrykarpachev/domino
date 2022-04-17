def upper_letters(f):
    def wrapper(*args):
        f(args[0].upper())
    return wrapper


@upper_letters
def func(txt):
    print(txt)


In = input()
func(In)
