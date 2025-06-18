import sys

expr = input("EXPRESSION: ")
expr_list = expr.split()
number_stack = []
operators = ["+","-","*","/","**","//","%"]
for i in expr_list:
    if i.isdigit():
        number_stack.append(i)
    elif i in operators:
        if len(number_stack) < 2:
            print("INVALID SYNTAX")
            sys.exit()
        number1 = number_stack.pop()
        number2 = number_stack.pop()
        number_stack.append(str(eval(number2+i+number1)))
    elif i.isalpha() or i in "<>;:!@#$&_=~`":
        print(f"INVALID SYNTAX {i}")
        sys.exit()
    else:
        continue
    
print(int(str(number_stack).strip("[\']")))