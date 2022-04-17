def tagged(f):
    def wrapper(*args):
        print(f'<title>{f(args[0])}</title>')
    return wrapper


@tagged
def func(txt):
    return txt.strip()


func(input())
