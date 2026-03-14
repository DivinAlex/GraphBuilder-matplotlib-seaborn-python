import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt
import seaborn as sb
import pandas as pd


def dataframe(x,y):
    data = {}
    x_a = []
    y_a = []
    k = int(input("ammount of values:"))
    for i in range(k):
        t = float(input(f"value {i+1} in (x):"))
        x_a.append(t)
    for i in range(k):
        t = float(input(f"value {i+1} in (y):"))
        y_a.append(t)
    data[x] = x_a
    data[y] = y_a
    return data


def diagframe(n):
    vars = []
    values = []
    for i in range(n):
        v = input(f"Variable №{i+1}:")
        vars.append(v)
        val = float(input(f"Value for {v}"))
        values.append(val)
    return pd.DataFrame({'Category':vars,'Data':values})


graphname = str(input("Graph name:"))
plottype = str(input("please type plot type here(Bar,Line,Diagram):")).strip().capitalize()
if plottype == "Diagram":
    number_of_valriables = int(input("Please type here how many variables you want to see on diag:"))
    df = diagframe(number_of_valriables)
    plt.figure(figsize=(8,8))
    plt.pie(df['Data'],
            labels=df['Category'],
            autopct='%1.1f%%',
            colors = sb.color_palette('pastel'),
            startangle=140
            )
    plt.title(graphname)
    plt.show()
else:
    x = input("X Axis:")
    y = input("Y Axis:")


    dt = dataframe(x,y)


    df = pd.DataFrame(dt)

if plottype == "Line":
    sb.lineplot(data=df, x=x, y=y)
elif plottype == "Bar":
    sb.barplot(data=df, x=x, y=y)
elif plottype == "Diagram":
    sb.kdeplot(data=df, x=x, y=y)
plt.title(graphname)
plt.show()
