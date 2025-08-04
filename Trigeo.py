import sys

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

def arithmetics():

    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Back")

def quiz():
    while True:
        print("==========QUIZ==========")

def sub_menu():
    print("1. Start")
    print("2. Back")

def normal():
    print("==========Normal Calculator==========")
    while True:
        arithmetics()
        choice = input("Choose (1/2/3/4/5) or press q to quit: ").lower()
        if choice == "1":
            pass
        elif choice == "2":
            pass
        elif choice == "3":
            pass
        elif choice == "4":
            pass
        elif choice == "5":
            break
        elif choice == "q":
            sys.exit("Goodbye.")
        else:
            print("===Try again===")
            
def geo():
    while True:
        print("==========Geometry Calculator==========")
        pass

def trigo():
    while True:
        print("==========Trigonometry Calculator==========")
        pass

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

