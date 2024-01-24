import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn
from sklearn.linear_model import LinearRegression

df=pd.read_csv("../datasets/TVShows_new.csv")
print(df)

x = pd.DataFrame(df, columns = ["year"])
y = pd.DataFrame(df, columns = ['averageRating'])

plt.scatter(x,y, alpha = 0.3)
plt.xlabel("year")
plt.ylabel("averageRating")

plt.xlim(1950, 2020)
plt.ylim(0, 10)

plt.show()

linreg = LinearRegression()
linreg.fit(x,y)
linreg.coef_
linreg.intercept_
plt.scatter(x,y, alpha = 0.3) 

plt.xlabel("year")
plt.ylabel("minutes")

plt.plot(x, linreg.predict(x), color='yellow')

plt.xlim(1950, 2020)
plt.ylim(0, 10)


plt.show()