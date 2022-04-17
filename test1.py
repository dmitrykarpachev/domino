def morning(func):
    def wrapper(*args):
        func(args[0])
        print('Good morning,', args[0])
    return wrapper


@morning
def greetings(name):
    print('Hello,', name)


greetings(input())
