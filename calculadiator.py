# Calculation problems for kids

import random

def plus(a, b):
    s = answer()
    resault = a + b
    if s == resault:
        print(f"Well done, {resault} is the right answer.")
        return True
    else:
        print(f"Sorry, the right answer was {resault}.")
        return False

def minus(a, b):
    s = answer()
    resault = a - b
    if s == resault:
        print(f"Well done, {resault} is the right answer.")
        return True
    else:
        print(f"Sorry, the right answer was {resault}.")
        return False

def division(a, b):
    s = answer()
    resault = a // b
    if s == resault:
        print(f"Well done, {resault} is the right answer.")
        return True
    else:
        print(f"Sorry, the right answer was {resault}.")
        return False

def multiplication(a, b):
    s = answer()
    resault = a * b
    if s == resault:
        print(f"Well done, {resault} is the right answer.")
        return True
    else:
        print(f"Sorry, the right answer was {resault}.")
        return False
def svar():
    return int(input("Svar: "))

def main():
    counter = 1
    x = 0
    z = 0
    while counter < 11:
        print(f"Dæmi {counter}")
        if start == "+":
            t1 = 1
            t2 = 100
            t3 = 1
            t4 = 100
            number_1 = random.randint(t1, t2)
            number_2 = random.randint(t3, t4)
            print(f"What is {number_1} plus {number_2}")
            equals = plus(number_1, number_2)
        elif start == "-":
            t1 = 50
            t2 = 100
            t3 = 1
            t4 = 50
            number_1 = random.randint(t1, t2)
            number_2 = random.randint(t3, t4)
            print(f"What is {number_1} minus {number_2}")
            equals = minus(number_1, number_2)
        elif number == "*":
            t1 = 1
            t2 = 10
            t3 = 1
            t4 = 11
            number_1 = random.randint(t1, t2)
            number_2 = random.randint(t3, t4)
            print(f"What is {number_1} times {number_2}")
            equals = multiplication(number_1, number_2)
        elif start == "/":
            q = 1
            while q != 0:
                t1 = 4
                t2 = 50
                t3 = 2
                t4 = 4
                number_1 = random.randint(t1, t2)
                number_2 = random.randint(t3, t4)
                q = number_1 % number_2
                if q == 0:
                    print(f"What is {number_1} divided by {number_2}")
                    equals = division(number_1, number_2)
        else:
            print("OKAY")
        if equals:
            x += 1
        else:
            z += 1
        counter += 1
        print(f"Right answers {x}\nWrong answers {z}")
    if z == 0:
        print(f"Congratulations! Your score is {x}.")
    elif x == 0:
        print(f"You could do with a bit more practice, you scored {x}.")
    else:
        print(f"Your score is {x}. You had {z} wrong answers.")
        
# while start == True: # 1.step - users pick
#    try:    
start = input("Hi there and welcome to.....math... Push eather + - * or / to start.")
if start == "+" or "-" or "*" or "/":
    main()
#    except:
#        print("You have to choose eather + or - or * or / to begin.")
