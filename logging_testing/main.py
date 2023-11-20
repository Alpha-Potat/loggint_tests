import logging

from formats import CustomFormatter,JSONTo, RequestsHandler


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




def sum(a:int, b:int) -> int: return a+b
def sub(a:int, b:int) -> int: return a-b
def mult(a:int, b:int) -> int: return a*b
def div(a:int, b:int) -> int: return a/b


def main():
    x=int(input("X is: \n"))
    y=int(input("Y is: \n"))
    
    logger.debug(f"Add: {x} + {y} = {sum(x,y)}")
    logger.info(f"div: {x} / {y} = {div(x,y)}")
    logger.warning(f"div: {x} / {y} = {div(x,y)}")
    logger.error(f"Sub: {x} - {y} = {sub(x,y)}")
    logger.critical(f"Mult: {x} * {y} = {mult(x,y)}")
    logger.critical("Password : jgkfdh678.,")


    

if __name__=="__main__":
    main()
