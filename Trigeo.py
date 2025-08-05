import sys
import math

def calculators():
    print("==========Calculators==========")
    print("1. Normal")
    print("2. Geometry")
    print("3. Trigonometry")
    print("4. Back")

def show_menu():
    print("==========TriGeo Calculator==========")
    print("1. Calculators")
    print("2. Quiz")
    print("3. Quit")

def quiz():
    while True:
        print("==========QUIZ==========")

def sub_menu():
    print("1. Start")
    print("2. Back")

def arithmetics():
    print("==========Normal Calculator==========")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Back")

def cont_act():
    while True:
        cont = input("Quit? (y/n): ").lower()
        if cont == "y":
            return True
        elif cont == "n":
            return False
        else:
            print("Invalid input, try again.")

def normal():
    while True:
        arithmetics()
        choice = input("Choose (1/2/3/4/5) or press q to quit: ").lower()
        
        if choice == "1":
            while True:
                try:
                    print("\n==========Addition==========")
                    num1 = float(input("What's the first number: "))
                    num2 = float(input("What's the second number: "))
                    num1 += num2
                    print(f"{num1}")
                    if cont_act():
                        break
                except ValueError:
                    print("Invalid input, try again.")
                    
        elif choice == "2":
            while True:
                try:
                    print("\n==========Subtraction==========")
                    num1 = float(input("What's the first number: "))
                    num2 = float(input("What's the second number: "))
                    num1 -= num2
                    print(f"{num1}")
                    if cont_act():
                        break
                except ValueError:
                    print("Invalid input, try again.")
                    
        elif choice == "3":
            while True:
                try:
                    print("\n==========Multiplication==========")
                    num1 = float(input("What's the first number: "))
                    num2 = float(input("What's the second number: "))
                    num1 *= num2
                    print(f"{num1}")
                    if cont_act():
                        break
                except ValueError:
                    print("Invalid input, try again")
                    
        elif choice == "4":
            while True:
                try:
                    print("\n==========Division==========")
                    num1 = float(input("What's the first number: "))
                    num2 = float(input("What's the second number: "))
                    num1 /= num2
                    print(f"{num1}")
                    if cont_act():
                        break
                except ValueError:
                    print("Invalid input, try again.")
                    
        elif choice == "5":
            break
            
        elif choice == "q":
            sys.exit("Goodbye.")
            
        else:
            print("===Try again===")

def geo():
    while True:
        print("\n==========Geometry Calculator==========")
        print("1. Circle")
        print("2. Square")
        print("3. Triangle")
        print("4. Rectangle")
        print("5. Back")
        choice = input("Choose what you would like to solve or press q to quit: ").lower()
        
        if choice == "1":
            while True:
                try:
                    rad = float(input("Value of radius: "))
                    area = rad ** 2 * math.pi
                    print(f"The area is {round(area, 2)} unit²")
                    if cont_act():
                        break
                except ValueError:
                    print("Invalid input, try again.")
                    
        elif choice == "2":
            while True:
                try:
                    side = float(input("Value of the side: "))
                    area = side ** 2
                    print(f"The area is {round(area, 2)} unit²")
                    if cont_act():
                        break
                except ValueError:
                    print("Invalid input, try again.")
                    
        elif choice == "3":
            while True:
                try:
                    base = float(input("Value of the base: "))
                    height = float(input("Value of the height: "))
                    area = base * height / 2
                    print(f"The area is {round(area, 2)} unit²")
                    if cont_act():
                        break
                except ValueError:
                    print("Invalid input, try again")
                    
        elif choice == "4":
            while True:
                try:
                    base = float(input("Value of the base: "))
                    height = float(input("Value of the height: "))
                    area = base * height
                    print(f"The area is {round(area, 2)} unit²")
                    if cont_act():
                        break
                except ValueError:
                    print("Invalid input, try again")
                    
        elif choice == "5":
            break
            
        elif choice == "q":
            sys.exit("Goodbye.")
            
        else:
            print("===Try again===")

def trigo():
    while True:
        print("==========Trigonometry Calculator==========")
        print("1. Scalene")
        print("2. Isosceles")
        print("3. Equilateral")
        print("4. Back")
        choice = input("Choose what you would like to solve or press q to quit: ")

        if choice == "1":
            bh_conf = input("Are the base and height given? (y/n): ").lower()
            if bh_conf == "y":
                while True:
                    try:
                        base = float(input("Value of the base: "))
                        height = float(input("Value of the height: "))
                        area = round(base * height / 2, 2)
                        print(f"The area is {area} unit²")
                        if cont_act():
                            break
                    except ValueError:
                        print("Invalid input, try again")
            elif bh_conf == "n":
                semi_p = input("Is semi-perimeter given? (y/n): ").lower()
                if semi_p == "y":
                    while True:
                        try:
                            s = float(input("Value of the semi-perimeter: "))
                            side_a = float(input("value of side a: "))
                            side_b = float(input("value of side b: "))
                            side_c = float(input("value of side c: "))
                            if (side_a + side_b > side_c) and (side_a + side_c > side_b) and (side_b + side_c > side_a):
                                area = round(math.sqrt(s * (s - side_a) * (s - side_b) * (s - side_c)), 2)
                                if area >= 0:
                                    print(f"The area is {area} unit²")
                                    if cont_act():
                                        break
                                else:
                                    print("Math error: Negative inside the square root.")
                            else:
                                print("Math error")
                        except ValueError:
                            print("Invalid input, try again")

                elif semi_p == "n":
                    while True:
                        try:
                            side_a = float(input("value of side a: "))
                            side_b = float(input("value of side b: "))
                            side_c = float(input("value of side c: "))
                            if (side_a + side_b > side_c) and (side_a + side_c > side_b) and (side_b + side_c > side_a):
                                sval = (side_a + side_b + side_c) / 2
                                area = round(math.sqrt(sval * (sval - side_a) * (sval - side_b) * (sval - side_c)), 2)
                                if area >= 0:
                                    print(f"The area is {area} unit²")
                                    if cont_act():
                                        break
                                else:
                                    print("Math error: Negative inside the square root.")
                            else:
                                print("Math error.")
                        except ValueError:
                            print("Invalid input, try again")
                else:
                    print("Invalid input, try again.")
            else:
                print("Invalid input, try again.")

        elif choice == "2":
            bh_conf = input("Are the base and height given? (y/n): ").lower()
            if bh_conf == "y":
                while True:
                    try:
                        base = float(input("Value of the base: "))
                        height = float(input("Value of the height: "))
                        area = round(base * height / 2, 2)
                        print(f"The area is {area} unit²")
                        if cont_act():
                            break
                    except ValueError:
                        print("Invalid input, try again")
            elif bh_conf == "n":
                while True:
                    try:
                        side_a = float(input("Value of side a: "))
                        side_b = float(input("Value of side b: "))
                        area = round(side_b * math.sqrt(side_a ** 2 - side_b ** 2 / 4) / 2, 2)
                        print(f"The area is {area} unit²")
                        if cont_act():
                            break
                    except ValueError:
                        print("Invalid input, try again")
            else:
                print("Invalid input, try again.")

        elif choice == "3":
            while True:
                try:
                    side = float(input("Value of the side: "))
                    area = round(side ** 2 * math.sqrt(3) / 4, 2)
                    print(f"The area is {area} unit²")
                    if cont_act():
                        break
                except ValueError:
                    print("Invalid input, try again")

        elif choice == "4":
            break

        elif choice == "q":
            sys.exit("Goodbye.")

        else:
            print("===Try again===")

def main():
    while True:
        show_menu()
        try:
            choice = int(input("Choose what to do (1/2/3): "))
            if choice == 1:
                while True:
                    calculators()
                    calc = input("Choose a calculator (1/2/3/4) or press q to quit: ").lower()
                    if calc == "1":
                        while True:
                            print("==========Normal Calculator==========")
                            sub_menu()
                            choice = input("Choose (1/2) or press q to quit: ").lower()
                            if choice == "1":
                                normal()
                            elif choice == "2":
                                break
                            elif choice == "q":
                                sys.exit("Goodbye.")
                            else:
                                print("===Try again===")
                    elif calc == "2":
                        while True:
                            print("==========Geometry Calculator==========")
                            sub_menu()
                            choice = input("Choose (1/2) or press q to quit: ").lower()
                            if choice == "1":
                                geo()
                            elif choice == "2":
                                break
                            elif choice == "q":
                                sys.exit("Goodbye.")
                            else:
                                print("===Try again===")
                    elif calc == "3":
                        while True:
                            print("==========Trigonometry Calculator==========")
                            sub_menu()
                            choice = input("Choose (1/2) or press q to quit: ").lower()
                            if choice == "1":
                                trigo()
                            elif choice == "2":
                                break
                            elif choice == "q":
                                sys.exit("Goodbye.")
                            else:
                                print("===Try again===")
                    elif calc == "4":
                        break
                    elif calc == "q":
                        sys.exit("Goodbye.")
                    else:
                        print("===Try again===")
            elif choice == 2:
                quiz()
            elif choice == 3:
                print("Goodbye!")
                break
            else:
                print("===Try again===")
        except ValueError:
            print("=====Enter a valid input=====")

main()
