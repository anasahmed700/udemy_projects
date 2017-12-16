# slicing 1
string = 'thisisateststringforslicer'

# slice test from string
print(string[string.index('test'): string.index('string')])

# get user email address
email = input('What is your email?: ')

# slice out user name
user = email[:email.index('@')]

# slice domain name
domain = email[email.index('@')+1: email.index('.')]

# format message
message = 'Your user name is {} and your domain name is {}.'.format(user, domain)

# display output message
print(message)