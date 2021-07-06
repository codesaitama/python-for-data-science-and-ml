seq = [1,2,3,4,5]

def square(num: int):
    '''
    Function squares a number.
    '''
    return num ** 2

# Lambda version of the square function
lambda_square = lambda num : num * 2

print(list(map(square, seq)))