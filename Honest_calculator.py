from operator import contains

# All messages
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

msg_ = [msg_1, msg_2, msg_3, msg_4, msg_5, msg_6, msg_7, msg_8, msg_9, msg_10, msg_11, msg_12]      # Messages list

memory = 0      # Memory constant

# Asks user if he wants to save value into memory for next calculations
def check_save(result, memory):    
    print(msg_4)
    answer = input()
    msg_index = 10
    M = memory

    if answer == "y" and is_one_digit(result) != True:
        M = result    
    if answer == "y" and is_one_digit(result) == True:
        while is_one_digit(result):        
            print(msg_[msg_index-1])
            answer = input()
            if answer == "y":
                if msg_index < 12:
                    msg_index += 1
                else:
                    M = result
                    break;
            elif answer == "n":
                break;
    else:
        pass;
 
    return M

# Asks user if he wants to continue using calculator
def check_continue():
    while True:
        print(msg_5)
        answer = input()
        if answer == "y":
            break;
        elif answer == "n":
            break;
        else:
            pass;

# Checks if number is integer (Including .0 float values)
def is_integer(value):
    string = str(value)
    if string.__contains__(".") and (value - int(value) != 0):
        return False
    if string.__contains__(".") == False and (value - int(value) == 0):
        return True
    else:
        return True
        
# Checks if the value has one digit (Including .0 float values)    
def is_one_digit(value):
    if float(value) > -10 and float(value) < 10 and is_integer(value):
        output = True
    else:
        output = False
    return output

# Troll messages
def check(v1, v2, v3):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg += msg_6
    if ((v1) == "1" or (v2) == "1" or int(v1) == 1 or int(v2) == 1) and v3 == "*":
        msg += msg_7
    if (v3 == "*" or v3 == "+" or v3 =="-") and ((v1) == "0" or (v2) == "0" or int(v1) == 0 or int(v2) == 0):
        msg += msg_8
    if msg != "":
        msg = msg_9 + msg
    print(msg)


# MAIN part
while True:

    print(msg_0)
    original_equation = input()     # Acceptable only in form: "num operator num" i.e. "5 + 10"
    
    equation_list = original_equation.split()   # List storing split words of input   
    result = 0  
    first_number = 0
    second_number = 0
    
    try:
        # Checking the input if it is int/float/memory
        # First number, coordinate 0 of list
        if equation_list[0].__contains__(".") == True:
            equation_list[0] = float(equation_list[0])
            first_number = equation_list[0]
        elif equation_list[0] == "M":
            equation_list[0] = memory
            first_number = equation_list[0]
        else:
            equation_list[0] = int(equation_list[0])
            first_number = equation_list[0]
         
        # Second number, coordinate 2 of list
        if equation_list[2].__contains__(".") == True:
            equation_list[2] = float(equation_list[2])
            second_number = equation_list[2]
        elif equation_list[2] == "M":
            equation_list[2] = memory
            second_number = equation_list[2]
        else:
            equation_list[2] = int(equation_list[2])
            second_number = equation_list[2]
         
        # Troll function
        check(equation_list[0],equation_list[2],equation_list[1])
           
        
        # Checks operation on coordinate 1 of list
        if equation_list[1] == "+":
            result = first_number + second_number
            print(float(result))    # Result can be only saved as float value
            memory = check_save(result, memory)            
            while True:
                print(msg_5)
                answer = input()
                if answer == "y":
                    break;
                elif answer == "n":
                    break;
                else:
                    pass;
            if answer == "n":
                break;
                
        elif equation_list[1] == "-":
            result = first_number - second_number
            print(float(result))
            memory = check_save(result, memory)
            while True:
                print(msg_5)
                answer = input()
                if answer == "y":
                    break;
                elif answer == "n":
                    break;
                else:
                    pass;
            if answer == "n":
                break;
            
        elif equation_list[1] == "*":
            result = first_number * second_number
            print(float(result))
            memory = check_save(result, memory)
            while True:
                print(msg_5)
                answer = input()
                if answer == "y":
                    break;
                elif answer == "n":
                    break;
                else:
                    pass;
            if answer == "n":
                break;
            
        elif equation_list[1] == "/":
            result = first_number / second_number
            print(float(result))
            memory = check_save(result, memory)
            while True:
                print(msg_5)
                answer = input()
                if answer == "y":
                    break;
                elif answer == "n":
                    break;
                else:
                    pass;
            if answer == "n":
                break;
            
        else:
            print(msg_2)    # If operators are wrong or non existing
            continue;

        
        
    except ValueError:
        print(msg_1)    # If num is not number but rather character
        continue;
    except ZeroDivisionError:
        print(msg_3)
        continue;


    