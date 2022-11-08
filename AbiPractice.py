# Codes to test

def assing_1(Statement):
    pass

input = 'The quick Brown Fox'
output_upper = []
output_lower = []
for Char in input:
    print(Char)

for Char in input:
    output_upper.append(Char.isupper())
    output_lower.append(Char.islower())
print(sum(output_upper))
print(sum(output_lower))

