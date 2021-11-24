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
    
    calls_transposed = list(map(list, zip(*calls)))
    texts_transposed = list(map(list, zip(*texts)))
    count = len(set(calls_transposed[0]).union(set(calls_transposed[1]), 
        set(texts_transposed[0]), set(texts_transposed[1])))

    print("There are {} different telephone numbers in the records.".format(count))

# %%
count_unique_numbers(texts, calls)

# %%
"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
