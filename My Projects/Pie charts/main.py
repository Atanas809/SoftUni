# Pie charts using library (matplotlib):

import matplotlib.pyplot as pyplot

labels = ('Python', 'Java', 'JS', 'C#')
sizes = [45, 30, 15, 10]
pyplot.pie(sizes,
           labels=labels,
