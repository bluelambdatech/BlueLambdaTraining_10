"""
Write a Python function that accepts a string and calculate the number of upper
case letters and lower case letters. Go to the editor
Sample String: 'The quick Brow Fox'
Expected Output:
No. of Upper case characters: 3
No. of Lower case characters: 12

"""


def assign_1(statement):
    """
    Write a Python function that accepts a string and calculate the number of upper
    case letters and lower case letters. Go to the editor

    :statement: str -> To count the upper and lower case characters
    :return: None
    Sample String: 'The quick Brow Fox'
        Expected Output:
        No. of Upper case characters: 3
        No. of Lower case characters: 12
    """
    upper = sum([char.isupper() for char in statement])
    lower = sum([char.islower() for char in statement])
    print(f' No of Upper case characters: {upper}')
    print(f' No of Lower case characters: {lower}')


def assign_2(statement):
    """
        Write a Python function that accepts a string and calculate the number of upper
        case letters and lower case letters. Go to the editor

        :statement: str -> To count the upper and lower case characters
        :return: Tuple
        Sample String: 'The quick Brow Fox'
            Expected Output:
            No. of Upper case characters: 3
            No. of Lower case characters: 12
        """
    upper = sum([char.isupper() for char in statement])
    lower = sum([char.islower() for char in statement])
    return upper, lower


x, y = assign_2('The quick Brow Fox')

print(x)





# inp = ' The quick Brow Fox'
# output_upper = []
# output_lower = []
# for char in inp:
#     output_upper.append(char.isupper())
#     output_lower.append(char.islower())
# print(sum(output_upper))
# print(sum(output_lower))
#
# print(sum([char.isupper() for char in inp]))
# print(sum([char.islower() for char in inp]))

#print(assign_1('The quick Brow Fox'))