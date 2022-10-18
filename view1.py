import model1
import logger
def view_data(data):
    logger.logger((f"{model1.exp} = {data}"))
    print((f"{model1.exp} = {data}"))
def get_value():
    return (input("Ввдете выражение: "))
