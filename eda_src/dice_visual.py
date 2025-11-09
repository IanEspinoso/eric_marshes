import plotly.express as px

from die import Die

# Creates two D6 dice
die_1 = Die()
die_2 = Die()

# Runs some tests and stores thte results in a list
results = []
for roll_num in range(1_000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analizes the results
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
poss_results = range(2, max_result+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualizes the results
title = "Results of Rolling Two D6 Dice 1,000 Times"
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

# Further personalizes the chart
fig.update_layout(xaxis_dtick=1)

fig.show()