import math
import matplotlib.pyplot as plt 
def successive_differentiation(mu,alpha):
    i=0
    f=[]
    t=[]
    dio=[]
    dfo=[]
    while(i<10):
        t.append(i)
        f.append(pow(t[-1],mu))
        dio.append(mu*pow(t[-1],mu-1))
        dfo.append((math.gamma(mu+1)/math.gamma(mu-alpha+1))*pow(t[-1],(mu-alpha)))
        i+=0.01

    print(len(t),len(f),len(dio),len(dfo))
    plt.plot(t,f,color="blue")
    plt.plot(t,dio,color="red")
    plt.plot(t,dfo,color="green")
    plt.show()
successive_differentiation(1.2,0.1)
