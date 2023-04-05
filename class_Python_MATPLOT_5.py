import matplotlib.pyplot as plt
import numpy as np
import random
import seaborn as sns

#ROLLING THE DIE AND CALCULATING DIE FREQUENCIES
rolls = [random.randrange(1,7) for i in range(600)]
values, frequencies = np.unique(rolls, return_counts=True)

#CREATING THE INITIAL BAR PLOT
title = f'Rolling a Six-Sided DIe {len(rolls):,} Times'
sns.set_style('whitegrid')
axes = sns.barplot(x=values, y = frequencies, palette= 'bright')

#Setting the window Title and Labelling the x-axis and y-axis

axes.set_title(title)

axes.set(xlabel ='Die Value', ylabel ='Frequency')

#FINANLIZING THE BAR PLOT
#displaying the text 
axes.set_ylim(top=max(frequencies) * 1.10)
for bar, frequency in zip(axes.patches, frequencies):
    text_x = bar.get_x() + bar.get_width() / 2.0
    text_y = bar.get_height()
    text = f'{frequency:,}\n{frequency / len(rolls):.3%}'
    axes.text(text_x, text_y, text, fontsize=11, ha='center', va='bottom')

