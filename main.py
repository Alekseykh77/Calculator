import controller
import model
import view
import controller1
choice = int(input('''
    Выберите формат калькулятора:
    
    1. Строчный 
    2. Числовой 
    
    '''))
if choice == 1:
        controller1.button_click()
                
elif choice == 2:
        model.init_first()
        while True:
            if model.init_ops():
                break
            model.init_second()
            controller.operation()
            view.print_total()
            model.first = model.total
