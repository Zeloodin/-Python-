import logging

logging.basicConfig(filename=f"{__name__}_errors.log",
                    filemode="a",
                    level=logging.ERROR,
                    encoding="utf-8", # Unexpected argument(s)
                    )

def some_func(a,b) -> None | float:
    try:
        return a/b
    except ZeroDivisionError as e:
        print("error")
        logging.error(f"При аргументах {a}/{b} возникла |{e}|")
        return None

if __name__ == "__main__":
    print("run code")
    some_func(1,2)
    some_func(3,0)