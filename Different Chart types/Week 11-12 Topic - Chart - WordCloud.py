# Week 11-12 Topic - Chart - WordCloud

from wordcloud import WordCloud
import matplotlib.pyplot as plt

words = ("This course was Fun I learned so much and these python are now just random words Fun so I am saying Good day to every one two three four five six seven eight nine ten")

wordcloud = WordCloud(width = 480, height = 480, margin = 0).generate(words)

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.margins(x=0, y=0)
plt.show()
