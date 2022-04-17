def print_info(func):
    def wrapper(*args):
        print(*args)
        func(*args)
    return wrapper


@print_info
def function(x1, x2):
    print(x1 + x2)


function(22, 25)
