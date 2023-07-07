Regex_Pattern = r"\d\d\D\d\d\D\d\d\d\d"	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
     

a = "0-9a-b.,"
len(a)
     


Regex_Pattern = r'^[123][0-2][xs0][30Aa][xsu][\.,]$'	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())