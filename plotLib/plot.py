import plotly.graph_objs as go
import plotly.offline as ply


alpha=float(input("Enter value of Alpha: "))
xRange=float(input("Enter max_value of x [0,x]: "))
stepSize=float(input("Enter Step-size : "))

data=[]


def returnEquation(coefficients,powers):
    form_equation=""
    for i in range(0,len(powers)):
        if coefficients[i]>=0 and i>0:
            form_equation+="+"+str(coefficients[i])+"*x"*powers[i]
        else:
            form_equation+=str(coefficients[i])+"*x"*powers[i]
    return form_equation


def setLayout(equation):
    layout = go.Layout(
    title=go.layout.Title(
        text='Fractional Derivative of '+equation,
        xref='paper',
        x=0
    ),
    xaxis=go.layout.XAxis(
        title=go.layout.xaxis.Title(
            text='t',
            font=dict(
                family='Courier New, monospace',
                size=18,
                color='#7f7f7f'
            )
        )
    ),
    yaxis=go.layout.YAxis(
        title=go.layout.yaxis.Title(
            text='f / dio / dfo',
            font=dict(
                family='Courier New, monospace',
                size=18,
                color='#7f7f7f'
                )
            )
        )
    )
    return layout

def plotFvsT(coefficients,powers):
    form_equation=returnEquation(coefficients,powers)
    f=[]
    t=[]
    
    x=0.0
    while x<=xRange:
        t.append(x)
        f.append(eval(form_equation))
        x=x+stepSize
    trace1=go.Scatter(x=t,y=f,line={'color':'blue'},name="t-f")
    data.append(trace1)
    return form_equation
    #print(t,f)


Equation=plotFvsT([10,5,3],[5,2,1])

layout=setLayout(Equation)

fig=go.Figure(data,layout)
    

ply.plot(fig,"render.html")



    
