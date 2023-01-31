import random

def main():
    number = random.randint(1, 5)
    for i in range(10):
        guess = input("try to choose the same integrer than the computer: ")
        if number == int(guess):
            print("nice shoot that s the same")
            break

if __name__=="__main__":
    main()