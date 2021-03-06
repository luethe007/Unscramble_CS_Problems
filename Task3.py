"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
# %%
import csv
import re

with open('data/texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('data/calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

# %% 
def get_area_codes(calls: list):
  # Loops through calls and prints area codes of to_numbers called from Bangalore
  codes = set()

  p_fixed_regex = re.compile("\(0\d+\)")

  for call in calls:
    if call[0].startswith("(080)"):
      to_number = call[1]
      result = p_fixed_regex.search(to_number)
      if result:
        codes.add(result.group(0))
      elif " " in to_number:
        codes.add(to_number.split(" ")[0][:4])
      else:
        codes.add("140")

  for code in sorted(codes):
    print(code)

def get_bangalore_ratio(calls: list):
  count = 0
  bangalore_count = 0

  for call in calls:
    if call[0].startswith("(080)"):
      count += 1
      if call[1].startswith("(080)"):
        bangalore_count += 1
  ratio = round((bangalore_count / count)*100, 2)

  print("{} percent of calls from fixed lines in Bangalore are calls \
    to other fixed lines in Bangalore.".format(ratio))

# %%
get_area_codes(calls)

# %%
get_bangalore_ratio(calls)

# %%
"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
