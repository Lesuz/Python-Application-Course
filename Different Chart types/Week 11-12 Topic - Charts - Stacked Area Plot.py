# Week 11-12 Topic - Charts - Lollipop PLot

import numpy as np
import matplotlib.pyplot as plt

x = ["Q1","Q2","Q3","Q4"]
y =[[102,87,65,130],[115,78,89,110],[120,80,125,115],[135,112,89,130]]

plt.stackplot(x,y, labels=["Tablet","Phone", "Laptop","Desktop Computer"])
plt.legend(loc="upper left")

plt.title("Product Sold in a Year divided into Quarters")
plt.show()