"""
input = “0001101000110100011110110111001111100”
Prefix Binary code: a code (eg. 101) cannot be prefix of another (no other code starts with 101)
' ' 101
'e' 1100
'g' 00
'h' 1101
'o' 01
'p' 1110
'r' 1111
's' 100
output = ‘go go gophers’
"""

mapping = {
    "101": " ",
    "1100": "e",
    "00": "g",
    "1101": "h",
    "01": "o",
    "1110": "p",
    "1111": "r",
    "100": "s"
}

input = "0001101000110100011110110111001111100"

seq = list(input)  # store the sequence into list
s1 = ""  # for temporary store
s2 = ""

for ind in input:
    s1 += seq.pop(0)  # pop the index element from list
    if s1 in mapping.keys():
        s2 += mapping[s1]
        s1 = ""
output = s2

print(output)