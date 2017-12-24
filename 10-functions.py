def rev(word):
    return word[::-1]

a = rev("pen")
print(a)

def add(*numbers): # * to use many arguments
    total = 0
    for number in numbers:
        total = total + number
    return total
print(add(1,3,4,5,7,8))


def about(name, age, likes):
    sentence = "meet {}! he is {} years old and he likes {}".format(name, age, likes)
    return sentence

dictionary = {"name": "Anas", "age": 24, "likes": "python"}
print(about(**dictionary)) # ** to use keyword arguments


def gender(**kwargs):
    for key, value in kwargs.items():
        print( '{}:{}'.format(key, value))
print(gender(Anas = "male", Huda = "female", Ali = "male"))