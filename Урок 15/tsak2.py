import logging
from functools import wraps

FORMAT = '| %(asctime)s | %(funcName)s | %(levelname)s | %(message)s'



logging.basicConfig(filename=f"task2_log.log",
                    filemode="a",
                    level=logging.DEBUG,
                    encoding="utf-8", # Unexpected argument(s),
                    format=FORMAT
                    )

def logging_deco(func):

    @wraps(func)
    def wrapper(*args,**kwargs):
        result  = func(*args,**kwargs)
        logging.debug(f"Аргументы: |{args}|{kwargs}| Результат: {result} "
                      f"| Функция {func.__name__}|")
        return result
    return wrapper

@logging_deco
def some_func(a: int | float,b: int | float) -> None | float:
    try:
        return a/b
    except ZeroDivisionError:
        return None

if __name__ == "__main__":
    # some_func(1, 2)
    # some_func(3, 0)
    for i,j in [(i,j) for i in range(1,10) for j in range(0,10)]:
        some_func(i,j)



















