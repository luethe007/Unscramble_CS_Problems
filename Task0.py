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
def get_first_text(texts: list):
    # Fetches the first text record and prints to terminal
    first_text = texts[0]
    print("First record of texts, {} texts {} at time {}".format(first_text[0],
        first_text[1], first_text[2]))

def get_last_call(calls: list):
    # Fetches the last call record and prints to terminal
    last_call = calls[-1]
    print("Last record of calls, {} calls {} at time {}, lasting {} seconds".format(last_call[0],
        last_call[1], last_call[2], last_call[3]))

# %% 
get_first_text(texts)
get_last_call(calls)


# %%
"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""
