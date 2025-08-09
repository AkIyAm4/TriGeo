import sys
import math

def calculators():
    print("\n==========Calculators==========")
    print("1. Normal")
    print("2. Geometry")
    print("3. Trigonometry")
    print("4. Back")

def show_menu():
    print("\n==========TriGeo Calculator==========")
    print("1. Calculators")
    print("2. Quiz")
    print("3. Quit")

def quiz():
    questions = ["What is the value of 45 ÷ (3 × 3)?",
                "What is 25% of 160?",
                "If x = 4, what is the value of 2x²-3x+1?",
                "What is the least common multiple (LCM) of 6 and 8?",
                "Simplify: 3/5 + 2/10",
                "What is the area of a triangle with base 10 cm and height 8 cm?",
                "What is the area of a circle with radius 7 cm?",
                "What is the area of a square with side length 12 cm?",
                "A rectangle has a length of 15 cm and width of 6 cm. What is its area?",
                "What is the area of a triangle with base 14 cm and height 5 cm?",
                "What is the area of a scalene triangle with sides 7 cm, 8 cm, and 9 cm?",
                "What is the area of an equilateral triangle with side 10 cm?",
                "An isosceles triangle has two equal sides of 13 cm and a base of 10 cm. What is its area?",
                "What is the area of a scalene triangle with sides 6 cm, 8 cm, and 10 cm?",
                "What is the area of an equilateral triangle with side length 6 cm?",]
    options = (("A. 5", "B. 6", "C. 4", "D. 3"),
               ("A. 35", "B. 45", "C. 40", "D. 50"),
               ("A. 21", "B. 25", "C. 19", "D. 24"),
               ("A. 24", "B. 12", "C. 48", "D. 48"),
               ("A. 5/10", "B. 4/5", "C. 1/2", "D. 7/10"),
               ("A. 40 cm²", "B. 80 cm²", "C. 60 cm²", "D. 50 cm²"),
               ("A. 154 cm²", "B. 144 cm²", "C. 147 cm²", "D. 132 cm²"),
               ("A. 124 cm²", "B. 144 cm²", "C. 132 cm²", "D. 156 cm²"),
               ("A. 90 cm²", "B. 80 cm²", "C. 85 cm²", "D. 96 cm²"),
               ("A. 35 cm²", "B. 70 cm²", "C. 45 cm²", "D. 60 cm²"),
               ("A. 26.83 cm²", "B. 30.05 cm²", "C. 28.15 cm²", "D. 31.2 cm²"),
               ("A. 42.5 cm²", "B. 43.3 cm²", "C. 45.2 cm²", "D. 50.0 cm²"),
               ("A. 72 cm²", "B. 60 cm²", "C. 65 cm²", "D. 62.4 cm²"),
               ("A. 24 cm²", "B. 25.2 cm²", "C. 22.8 cm²", "D. 26.1 cm²"),
               ("A. 15.6 cm²", "B. 16.5 cm²", "C. 15.59 cm²", "D. 17.2 cm²"))
    answers = ("A", "C", "A", "A", "B", "D", "A", "B", "A", "A", "C", "B", "D", "A", "C")
    guesses = []
    ques_num = 0
    score = 0
    for question in questions:
        print("\n==========QUIZ==========")
        print("--------------------------------------------------------------------------------")
        print(question)
        for option in options[ques_num]:
            print(option)
        guess = input("Enter your answer (A/B/C/D): ").upper()
        guesses.append(guess)
        if guess == answers[ques_num]:
            score += 1
            print("CORRECT!")
        else:
            print("INCORRECT!")
            print(f"{answers[ques_num]} is the correct answer.")
        ques_num += 1

    print()
    if score >= 11:
        print(f"Congratulations! Your score is {score}/{len(questions)}")
    elif score < 11:
        print(f"Your score is {score}/{len(questions)}. There's still room for improvement")
    elif score == 15:
        print(f"Excellent job! You got a perfect score!")
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

def handle_submenu(title, action_function):
    while True:
        print(f"\n=========={title}==========")
        sub_menu()
        choice = input("Choose (1/2) or press q to quit: ").lower()
        if choice == "1":
            action_function()
        elif choice == "2":
            break
        elif choice == "q":
            sys.exit("Goodbye.")
        else:
            print("===Try again===")

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
        print("\n==========Trigonometry Calculator==========")
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
                        handle_submenu("Normal Calculator", normal)
                    elif calc == "2":
                        handle_submenu("Geometry Calculator", geo)
                    elif calc == "3":
                        handle_submenu("Trigonometry Calculator", trigo)
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



