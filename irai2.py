import pandas as pd
import matplotlib.pyplot as plt

df1=pd.read_excel("D:\LATIHAN PANDAS SUMBER DATA\Tes Irai.xlsx", "CPO3")
x=df1['Year']
y1=df1["World GDP Quintrillion"]
y2=df1["Population Billion"]
y3=df1["Total Supply mmTon"]

plt.plot(x,y1, alpha=0.3,color='blue', label='World GDP in Quadrillion USD')
plt.plot(x,y2, alpha=0.3, color='red',label='Population in Billion')
plt.plot(x,y3, alpha=0.9, color='green',label='World CPO Supply in Million Metric Ton')
plt.xlabel('Year')
plt.title('World CPO Supply\n'+'by Sigit Wiendarto')
plt.legend()
plt.show()