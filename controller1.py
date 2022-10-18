import  model1
import view1
def button_click():
    value_a = view1.get_value()
    model1.init(value_a)
    result = model1.do_it()
    view1.view_data(result)
    