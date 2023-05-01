def my_decorator(func):
    def wrapper():
        print('Something happens before func()')
        func()
        print('Something happens afrer func()')
    return wrapper


def say_whee():
    print('Whee!!!')


if __name__ == '__main__':
    say_wheeeee = my_decorator(say_whee)
    print(type(say_wheeeee))
    say_wheeeee()
