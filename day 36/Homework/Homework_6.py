'''6. დაწერე ფუნქცია, რომელიც მიიღებს რიცხვების სიას და გამოიყვანს თითოეულს კვადრატში აყვანილს.'''

list_number = [12, 33, 367, 1293, 983, 23, 2]

def square(list):
    for i in range(len(list)):
        print(i ** 2)
square(list_number)