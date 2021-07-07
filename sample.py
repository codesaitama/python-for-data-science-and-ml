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

#Tuple unpacking
x = [(1, 2), (3, 4), (5, 6)]
    
for (a, b) in x:
    print(a)
    print(b)
    

'''
Create a function that grabs the email website domain from a string in the form: user@domain.com
So for example, passing "user@domain.com" would return: domain.com
'''    
def domainGet(email):
    return email.split('@')[1]

print(domainGet("user@domain.com"))

# Create a basic function that returns True if the word 'dog' is contained in the input string. Don't worry about edge cases like a punctuation being attached to the word dog, but do account for capitalization.
def findDog(words):
    return 'dog' in words

print(findDog('Is there a dog here?'))


# Create a function that counts the number of times the word "dog" occurs in a string. Again ignore edge cases.

def countDog(words):
    return len(words.split('dog')) - 1

print(countDog('This dog runs faster than the other dog dude!'))


'''
Use lambda expressions and the filter() function to filter out words from a list that don't start with the letter 's'. For example:

seq = ['soup','dog','salad','cat','great']
should be filtered down to:

['soup','salad']

'''

seq = ['soup','dog','salad','cat','great']

print(list(filter(lambda char: char[0] == 's', seq)))


'''
Final Problem
You are driving a little too fast, and a police officer stops you. Write a function to return one of 3 possible results: "No ticket", "Small ticket", or "Big Ticket". If your speed is 60 or less, the result is "No Ticket". If speed is between 61 and 80 inclusive, the result is "Small Ticket". If speed is 81 or more, the result is "Big Ticket". Unless it is your birthday (encoded as a boolean value in the parameters of the function) -- on your birthday, your speed can be 5 higher in all cases.
'''

def getSpeedingTicket(speed):
    if speed <= 60:
        return 'No Ticket'
    elif speed >= 61 and speed < 81:
        return 'Small Ticket'
    else:
        return 'Big Ticket'