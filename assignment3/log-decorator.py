# Task 1:
import logging

# logging set up:
logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log", "a"))

# logger_decorator:
def logger_decorator(func):
    
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        positional_output = args
        keyword_output = kwargs
        
        if args == ():
            positional_output = "none"
        if kwargs == {}:
            keyword_output = "none"

        # log
        logger.log(logging.INFO, f"""
        function: {func.__name__}
        positional parameters: {positional_output}
        keyword parameters: {keyword_output}
        return: {result}
        """)
        
        return result
    
    return wrapper

# functions
@logger_decorator
def greeting():
    print("Hello, World!")
    
@logger_decorator
def my_func(*args):
    return True

@logger_decorator
def another_func(**kwargs):
    return logger_decorator

greeting()
my_func(10)
another_func(name="Su", city="DC")