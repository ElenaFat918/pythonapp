x = 0   # модель тривиального калькулятора, в котором есть только два числа, их инициализация и логика складывания
y = 0

def init(a, b):     # метод, который отвечает за инициализацию значений 2х переменных
    global x    # вывели переменные за метод
    global y
    x = a
    y = b

def do_it(): # логика складывания
    return x + y