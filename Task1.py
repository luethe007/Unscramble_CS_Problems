"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
# %%
import csv
with open('data/texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('data/calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

# %%
def count_unique_numbers(texts: list, calls: list):
    # Counts the amount of unique phone numbers and prints to terminal
    
    numbers = set()
    for text in texts:
        numbers.update(set(text[:2]))
    for call in calls:
        numbers.update(set(call[:2]))

    print("There are {} different telephone numbers in the records.".format(len(numbers)))

# %%
count_unique_numbers(texts, calls)

# %%
"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
