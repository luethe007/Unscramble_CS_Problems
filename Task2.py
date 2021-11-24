"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
# %%
import csv
from collections import defaultdict
with open('data/texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('data/calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

def get_most_active_number(calls: list):
    # Computes the summed duration per phone number and prints to terminal
    
    phone_stats = defaultdict(lambda: 0)
    for call in calls:
        phone_stats[call[0]] += int(call[3])
        phone_stats[call[1]] += int(call[3])

    number = max(phone_stats, key=phone_stats.get)
    print("{} spent the longest time, {} \
        seconds, on the phone during September 2016.".format(number, phone_stats[number]))


# %%
get_most_active_number(calls)

# %%
"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

