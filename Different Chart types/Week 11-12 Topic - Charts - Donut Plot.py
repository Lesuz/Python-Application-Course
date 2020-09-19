# Week 11-12 Topic - Charts - Donut Plot

import matplotlib.pyplot as plt

class FavoritePets:

    pets = 'Dog {:.0f}'.format((13/38)*100) + '%','Cat {:.0f}'.format((15/38)*100) + '%','Hamster {:.0f}'.format((3/38)*100) + '%','Other {:.0f}'.format((5/38)*100) + '%'
    votes = [13,15,3,7]

    circle = plt.Circle( (0,0), 0.7, color='white')

    plt.xlabel("Class' favorite pets.")
    #Giving color for each pet
    plt.pie(votes, labels=pets, colors=['red','blue','skyblue','green'])
    p = plt.gcf()
    p.gca().add_artist(circle)
    plt.show()