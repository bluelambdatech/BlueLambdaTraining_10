"""
Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters. Go to the editor
Sample String : 'The quick Brow Fox'
Expected Output :
No. of Upper case characters : 3
No. of Lower case Characters : 12

print(sum(output_upper))
print(sum(output_lower))
print(len(inp) - sum(output_upper))
"""


def assign_1 (statement):
    print (sum([char.isupper() for char in statememt]))

# inp = 'The quick Brown Fox'
# output_upper = []
# output_lower = []
# for char in inp:
#     output_upper.append(char.isupper())
#     output_lower.append(char.islower)
#
# print(sum([char.isupper() for char in inp]))
# print(sum([char.islower() for char in inp]))

print (assign_1('OmolewA'))