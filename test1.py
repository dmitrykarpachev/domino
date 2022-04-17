def price_string(func):
    def wrapper(*args):
        print('₤' + func(args[0]))
    return wrapper


@price_string
def function(price):
    return str(price * 0.9)


function(100)
