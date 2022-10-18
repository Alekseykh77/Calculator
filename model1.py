exp = ""

def init(a):
    global exp
    exp = a

def do_it():
    complited_str = compile(exp,'string', 'eval')  
    res = eval(complited_str)
    return res
   