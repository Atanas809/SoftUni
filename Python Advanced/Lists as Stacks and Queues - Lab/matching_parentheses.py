expression = input()

my_stack = list()

for x in range(len(expression)):
    if expression[x] == "(":
        my_stack.append(x)
    elif expression[x] == ")":
        first_index = my_stack.pop()
        print(expression[first_index: x + 1])
