'''Assignment 1
This assignment covers your basic profiency with
    Python. It engages your ability to transform
    data without affecting anything outside the program.
This assignment places heavy emphasis on basic Python constructs.
'''

def factorial(x):
    '''Item 1.
    Factorial. 1 point.

    Returns the factorial of an integer.
    An integer's factorial is the product of the integer and all
        integers below it.
    Parameters
    ----------
    x: int
        the integer whose factorial to return
    Returns
    -------
    integer
        the factorial of the argument
    '''
    # Write your code below this line
    y = 1
    
    for i in range(2, x+1):
        y *= i
    return y


def classify_grade(number_grade):
    '''Item 2.
    Classify Grade. 2 points.

    Returns the letter grade equivalent of a number grade.
    For this item, use these letter grade buckets:
        A: 92-100
        B+: 86-91.9
        B: 80-85.9
        C+: 74-79.9
        C: 67-73.9
        D: 60-66.9
        F: 0-59.9
    Parameters
    ----------
    number_grade: float
        the number grade to convert into a letter grade.
    Returns
    -------
    str
        the letter grade equivalent of the number grade.
    '''
    # Write your code below this line
    if number_grade <= 100 and number_grade >= 92:
        return 'A'

    if number_grade <= 91.9 and number_grade >= 86:
        return 'B+'

    if number_grade <= 85.9 and number_grade >= 80:
        return 'B'

    if number_grade <= 79.9 and number_grade >= 74:
        return 'C+'

    if number_grade <= 73.9 and number_grade >= 67:
        return 'C'

    if number_grade <= 66.9 and number_grade >= 60:
        return 'D'

    if number_grade <= 59.9 and number_grade >= 0:
        return 'F'

    else:
        return 'Did you place the correct value?'

def average_weight(item_quantity_1, item_weight_1, item_quantity_2, item_weight_2):
    '''Item 3.
    Average Weight. 3 points.

    You have purchased two bags of items.
    The first bag contains one type of item, and the second bag contains another type.
    Return the weighted average weight of the items.

    Parameters
    ----------
    item_quantity_1: int
        the quantity of items in the first bag.
    item_weight_1: float
        the weight of each individual item in the first bag.
    item_quantity_2: int
        the quantity of items in the second bag.
    item_weight_2: float
        the weight of each individual item in the second bag.
    Returns
    -------
    float
        the weighted average weight of one item.
    '''
    # Write your code below this line
    return ((item_quantity_1 * item_weight_1) + (item_quantity_2 * item_weight_2)) / (item_weight_1 + item_weight_2)

def string_sum(string):
    '''Item 4.
    String Sum. 3 points.

    Returns the sum of the digits provided in a string.
    For this item:
        1. Sum the digits contained in the string.
        2. Ignore any non-digit characters contained in the string.
    Parameters
    ----------
    string: str
        a string that can contain any character.
    Returns
    -------
    int
        the sum of the digits contained in the string.
    '''
    # Write your code below this line
    temp = "0"
    Sum = 0
 
    for ch in string:
        if (ch.isdigit()):
            temp += ch
        else:
            Sum += int(temp)
            temp = "0"
    return Sum + int(temp)
    
def distance(x_1, y_1, x_2, y_2):
    '''Item 5.
    Distance. 3 points.
    Returns the distance between two points.
    To get the distance between two points:
        1. Get the difference between the two x-coordinates
        2. Get the difference between the two y-coordinates
        3. Sum the previous two values
        4. Return the square root of the sum
    You may want to import the `math` library for this number.
    Parameters
    ----------
    x_1: float
        the first x-coordinate
    y_1: float
        the first y-coordinate
    x_2: float
        the second x-coordinate
    y_2: float
        the second y-coordinate
    Returns
    -------
    float
        the distance between the two coordinates
    '''
    # Write your code below this line
    import math

    x_dist = abs(x_2 - x_1)
    y_dist = abs(y_2 - y_1)
    return math.sqrt(x_dist + y_dist)

def make_change(amount):
    '''Item 6.
    Make Change. 5 points.

    Return the combination of coins needed to make change for the given amount,
        which is given in centavos.
    For this item:
        1. You can return 1 peso, 25 centavos, 10 centavos, 5 centavos, and 1 centavo coins.
        2. Use the minimum number of coins possible.
    Parameters
    ----------
    amount: int
        the amount, in centavos, to make change for.
    Returns
    -------
    str
        the string representation of the change to be given.
        Format it like this:
            "1P:{amount}/25C:{amount}/10C:{amount}/5C:{amount}/1C:{amount}"
    '''
    # Write your code below this line
    whole = 0
    quarter = 0
    dime = 0
    nickle = 0
    penny = 0
    cursor = amount

    while cursor >= 1:
      whole += 1
      cursor -= 1
    cursor = amount-(1*whole)
    while cursor >= 0.25:
      quarter += 1
      cursor -= 0.25
    cursor = amount-(1.0*whole)-(0.25*quarter)
    while cursor >= 0.1:
      dime += 1
      cursor -= 0.1
    cursor = amount-(1*whole)-(0.25*quarter)-(0.1*dime)
    print(cursor)
    while cursor >= 0.05:
      nickle += 1
      cursor -= 0.05
    cursor = amount-(1*whole)-(0.25*quarter)-(0.1*dime)-(0.05*nickle)
    while cursor >= 0.01:
      penny += 1
      cursor -= 0.01

    print("1P:{}/25C:{}/10C:{}/5C:{}/1C:{}".format(whole, quarter, dime, nickle, penny))