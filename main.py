import regex as re


def isPossibleEquation(s):
    expression="([+-]?(?:(?:\d+x\^\d+)|(?:\d+x)|(?:\d+)|(?:x)))"

def menu():
    print("1)Enter Equation D^alpha (ax^n+bx^n-1+....+k) ")
    print("2)single...")
    print("3)Exit")

if __name__=="__main__":
    while(True):
        menu()
        choices=int(input("Enter choices"))
        if(choices==3):
            break
        elif choices==1:
            equation="10x^2+20x+3"



