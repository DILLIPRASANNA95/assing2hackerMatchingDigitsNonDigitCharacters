# assing2hackerMatchingDigitsNonDigitCharacters
he expression \d matches any digit [ - ].

ach04_01.png



The expression \D matches any character that is not a digit.

ach04_02.png


Task

You have a test string . Your task is to match the pattern 
Here  denotes a digit character, and  denotes a non-digit character.

Note

This is a regex only challenge. You are not required to write any code.
You only have to fill the regex pattern in the blank (_________).

Regex_Pattern = r"\d\d\D\d\d\D\d\d\d\d"    # Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
a = "0-9a-b.,"
len(a)
     
Regex_Pattern = r'^[123][0-2][xs0][30Aa][xsu][\.,]$'    # Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, raw_input()))).lower())
Input (stdin)
06-11-2015
Expected Output
true
