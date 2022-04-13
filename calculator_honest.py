msg_0 = "Enter an equation"

msg_1 = "Do you even know what numbers are? Stay focused!"

msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"

msg_3 = "Yeah... division by zero. Smart move..."

msg_4 = "Do you want to store the result? (y / n):" 

msg_5 = "Do you want to continue calculations? (y / n):"

msg_6 = " ... lazy"

msg_7 = " ... very lazy"

msg_8 = " ... very, very lazy"

msg_9 = "You are"

msg_10 = "Are you sure? It is only one digit! (y / n)"

msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"

msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"

operations = ["+", "-", "*", "/"]

memory = 0
result = 0

def is_one_digit(v):
    if (v < 10 and v > -10 and v.is_integer()):
        return True
    return False

def check(v1, v2, v3):
    msg = ""
    if (is_one_digit(v1) and is_one_digit(v2)):
        msg = msg + msg_6
    if ((v1 == 1 or v2 == 1) and v3 == "*"):
        msg = msg + msg_7
    if ((v1 == 0 or v2 == 0) and (v3 in ["+", "-", "*"])):
        msg = msg + msg_8
    if (msg != ""):
        msg = msg_9 + msg
        print(msg)
    return

def memory_store():
    global memory
    print(msg_4)
    answer = input()
    if answer == "y":
        if is_one_digit(result):
            msg_index = 10
            while(msg_index <= 12):
                print(globals()[f"msg_{msg_index}"])
                answer = input()
                if answer == "y":
                    msg_index = msg_index + 1
                elif answer == "n":
                    return
                
        memory = float(result)
    elif answer != "n":
        return memory_store()
    return
    
def calculation():
    print(msg_5)
    answer = input()
    if answer == "y":
        return calc()
    elif answer != "n":
        return calculation()
    return

def calc():
    global result
    global memory
    print(msg_0)
    x, oper, y = input().split()
    if x == "M":
        x = memory
    if y == "M":
        y = memory
    try:
        x = float(x)
        y = float(y)
    except ValueError:
        print(msg_1)
        return calc()
    if (oper not in operations):
        print(msg_2)
        return calc()
    check(x, y, oper)
    if oper == "+":
        result = x + y
    elif oper == "-":
        result = x - y
    elif oper == "*":
        result = x * y
    elif oper == "/":
        if y != 0:
            result = x / y
        else:
            print(msg_3)
            return calc()
    print(float(result))
    memory_store()
    return calculation()
calc()