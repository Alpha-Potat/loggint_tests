import logging
import time

from logging_testing.formats import CustomFormatter,JSONTo, RequestsHandler


fmt = "%(asctime)s type: %(levelname)s , and with message : %(message)s"


logger=logging.getLogger("myLogger")
logger.setLevel(logging.DEBUG)

terminal=logging.StreamHandler()
terminal.setFormatter(CustomFormatter(fmt))

file_handler=logging.FileHandler(f"1.json")
file_handler.setFormatter(JSONTo())

request_handler=RequestsHandler()
request_handler.setFormatter(JSONTo())

logger.addHandler(file_handler)
logger.addHandler(terminal)
logger.addHandler(request_handler)



def sum(a:(int, float), b:(int, float)) -> (int, float): 
    try:
        time.sleep(10)
        return a+b
    except(ValueError):
        raise TypeError("Args must be int or float")

def sub(a:(int, float), b:(int, float)) -> (int, float): 
    try:
        return a-b
    except(ValueError):
        raise TypeError("Args must be int or float")

def mult(a:(int, float), b:(int, float)) -> (int, float): 
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Args must be int or float")
        return a*b

def div(a:(int, float), b:(int, float)) -> (int, float): 
    try:
        return a/b
    except (ZeroDivisionError):
        raise ValueError("Value must not be zer0")
    except(ValueError):
        raise TypeError("Args must be int or float")


def main():
    try:
        x=float(input("X is: \n"))
        y=float(input("Y is: \n"))
        logger.debug(f"Add: {x} + {y} = {sum(x,y)}")
        logger.info(f"div: {x} / {y} = {div(x,y)}")
        logger.warning(f"div: {x} / {y} = {div(x,y)}")
        logger.error(f"Sub: {x} - {y} = {sub(x,y)}")
        logger.critical(f"Mult: {x} * {y} = {mult(x,y)}")
        logger.critical("Password : jgkfdh678.,")
    except:
        raise ValueError("Args must be int or float")


    

if __name__=="__main__":
    main()
