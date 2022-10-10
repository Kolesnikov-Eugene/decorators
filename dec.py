import datetime

def my_dec(some_function):
    def wrapper(*args, **kwargs):

        date_time = datetime.datetime.now()

        result = some_function(*args, **kwargs)

        with open ('log.txt', 'w') as f:
            f.write(f'Date and time of calling is {date_time} \n'
                    f'Name of function is {some_function.__name__} \n'
                    f'Arguments of function are {args} and {kwargs} \n'
                    f'Result is {result}')

        return result

    return wrapper

@my_dec
def power_of_nums(a, b):
    return a ** b

c = power_of_nums(2, 4)

