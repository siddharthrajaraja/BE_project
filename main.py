import regex as re
import Library.Fd_Successive_Differentiation as succDiff


class SolveThePolynomialEquation:
    coefficients=[]
    powers=[]

    def __init__(self,terms):
        print( "Terms we have are : " ,terms)
        for i in range(0,len(terms)):
            eachTerm=terms[i].split('x^')            
            if(len(eachTerm)!=1):
                self.coefficients.append(eval(eachTerm[0]))
                self.powers.append(eval(eachTerm[1]))
                
            else:
                self.coefficients.append(eval(eachTerm[0]))
                self.powers.append(0)
        #print(self.coefficients,self.powers)


        #succDiff.successive_differentiation(1.1,0.5)


def isPossibleEquation(s):
    expression=r'([+-]?(?:(?:\d+x\^\d+)|(?:\d+x)|(?:\d+)|(?:x)))'
    print(re.match(expression,s))
    if(re.match(expression,s)!=None):
        return True
    return False

def menu():
    print("1)Enter Equation D^alpha (ax^n+bx^n-1+....+k) ")
    print("2)single...")
    print("3)Exit")

def splitEachTerm(termsOfEquation):
    for i in range(0,len(termsOfEquation)):
        termsOfEquation[i]="".join(list(termsOfEquation[i]))
    return termsOfEquation
    
        

if __name__=="__main__":
    while(True):
        menu()
        choices=int(input("Enter choices"))
        if(choices==3):
            break
        elif choices==1:
            equation="9x^3+4x^2"
            if isPossibleEquation(equation):

                terms=splitEachTerm(re.findall(r'([0-9]+[x]*[\^]*[0-9]+)|([\+|\-|\*|\/]+[0-9]+[x]*[\^]*[0-9]+)',equation)) # This is to split each and every term of given polynomial equation.
                objectSolve=SolveThePolynomialEquation(terms)
            else:
                print("Invalid Equation")
            



