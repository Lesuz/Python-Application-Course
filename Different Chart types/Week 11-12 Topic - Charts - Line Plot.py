# Week 11-12 Topic - Charts - Line chart

from pylab import *
import matplotlib.pyplot as plt

class CovidCases:

    cases = [1685, 3565, 1864, 355, 218, 410]
    months = ['March', 'April', 'May', 'June', 'July', 'August']

    plot(months, cases, marker ='X')

    plt.xlabel("Month")
    plt.ylabel("Covid cases in Finland")

show()