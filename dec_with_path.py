import datetime

def dec_with_path(file_path):

    def my_dec(some_function):
        def wrapper(*args, **kwargs):

            date_time = datetime.datetime.now()

            result = some_function(*args, **kwargs)

            with open (file_path, 'w') as f:
                f.write(f'Date and time of calling is {date_time} \n'
                        f'Name of function is {some_function.__name__} \n'
                        f'Arguments of function are {args} and {kwargs} \n'
                        f'Result is {result}')

            return result

        return wrapper
    return my_dec

file_path = 'log_new.txt'

@dec_with_path(file_path)
def power_of_nums(a, b):
    return a ** b

c = power_of_nums(3, 10)
