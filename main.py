import sys
def rpn():
    expr = input("")
    expr_list = expr.split()
    number_stack = []
    operators = ["+","-","*","/","**","//","%"]
    for i in expr_list:
        if i.isdigit():
            number_stack.append(i)
        elif i in operators:
            if len(number_stack) < 2:
                print("INVALID SYNTAX")
                
            number1 = number_stack.pop()
            number2 = number_stack.pop()
            try:
                number_stack.append(str(eval(number2+i+number1)))
            except ZeroDivisionError as e:
                print(e)
                number_stack = []
        elif i.isalpha() or i in "<>;:!@#$&_=~`\"\'()[]{}":
            print(f"INVALID SYNTAX {i}")
            continue            
        else:
            continue

    if len(number_stack) == 1:
        print(int(str(number_stack).strip("[\']")))
    elif not len(number_stack):
        pass
    else:
        print("INVALID SYNTAX: leftover operands")
        
def main():
    while True:
        print(">>>",end = " ")
        rpn()

main()
