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
def get_telemarketers(calls: list, texts: list):
    # Extracts telemarketers from the datasets and prints to terminal
    calls_transposed = list(map(list, zip(*calls)))
    texts_transposed = list(map(list, zip(*texts)))

    telemarketers = set(calls_transposed[0]) - set(calls_transposed[1]) \
        - set(texts_transposed[0]) - set(texts_transposed[1])

    for telemarketer in sorted(telemarketers):
        print(telemarketer)

# %%
get_telemarketers(calls, texts)


# %%
"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

