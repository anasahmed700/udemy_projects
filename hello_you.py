# Ask user for name
name = input('what is your name?: ')

# Ask user for age
age = input('how old are you?: ')

# Ask user for city
city = input('what city do you live in?: ')

# Ask user for what they enjoy?
hobby = input('what do you love doing?: ')

# Create output text
string = 'your name is {} and you are {} years old. You live in {} and you love {}.'
output = string.format(name, age, city, hobby)

# Print output to screen
print(output)