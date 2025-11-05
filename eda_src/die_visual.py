from die import Die

# Creates a D6
die = Die()

# Runs some tests and stores the results in a list
results = []
for roll_num in range(100):
    result = die.roll()
    results.append(result)

print(results)