"""
Write a Python function that accepts a string and calculate the
number of upper case letters and lower case letters. Go to the editor
Sample String : 'The quick Brow Fox'
Expected Output :
No. of Upper case characters : 3
No. of Lower case Characters : 12
"""


def assign_1(statement):
    """
    Write a Python function that accepts a string and calculate the
    number of upper case letters and lower case letters. Go to the editor

    :statement: str -> The statement that you want to count the upper
        and lower
    :return: None

     Sample String : 'The quick Brow Fox'
        Expected Output :
        No. of Upper case characters : 3
        No. of Lower case Characters : 12
    """
    upper = sum([char.isupper() for char in statement])
    lower = sum([char.islower() for char in statement])
    print(f'No. of Upper case characters : {upper}')
    print(f'No. of Lower case Characters : {lower}')


def assign_2(statement):
    """
        Write a Python function that accepts a string and calculate the
        number of upper case letters and lower case letters. Go to the editor

        :statement: str -> The statement that you want to count the upper
            and lower
        :return: tuple -> 2 int values

         Sample String : 'The quick Brow Fox'
            Expected Output :
            No. of Upper case characters : 3
            No. of Lower case Characters : 12
        """
    upper = sum([char.isupper() for char in statement])
    lower = sum([char.islower() for char in statement])
    return lower, upper


x, y = assign_2('The quick Brow Fox')
