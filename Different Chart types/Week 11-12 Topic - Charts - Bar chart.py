# Week 11-12 Topic - Charts - Bar chart


import numpy as np
import matplotlib.pyplot as plt

class Grades:
 
    amount = [5, 3, 9, 3, 5]
    grade = ('1', '2', '3', '4', '5')
    y_pos = np.arange(len(grade))
 
    plt.bar(y_pos, amount)
 
    plt.xticks(y_pos, grade)

    plt.xlabel("Grade")
    plt.ylabel("Amount of students")
 
    # Show graphic

plt.show()