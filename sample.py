seq = [1,2,3,4,5]

def square(num: int):
    '''
    Function squares a number.
    '''
    return num ** 2

# Lambda version of the square function
lambda_square = lambda num : num ** 2

print(lambda_square(7))

#Using map
map_example = list(map(square, seq))
print(map_example)

#Using filter
filter_example = list(filter(lambda num: num % 2 == 0, seq))
print(filter_example)