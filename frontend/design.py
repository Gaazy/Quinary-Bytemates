#libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#create dataset
height = [2, 15, 5, 18]
bars = ('cleaning', 'breaks', 'tires', 'filters')
df = pd.DataFrame({
    'parts': bars,
    'time': height
})

#Create horizontal bars
plt.barh(y=df.parts, width=df.time)
#Show graphic
plt.savefig('my_plot.png')
plt.show()

