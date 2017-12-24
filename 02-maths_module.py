print('use of round function:')
x = 2.1
y = 1.5
print(round(x))
print(round(y))

import math
print('\nusage of floor() & ceil() functions:')
print(math.floor(y)) # this will return floor value of decimal point
print(math.ceil(x))  # this will return ceiling value of decimal point

print('\ntrigonometric functions')
x = math.pi/2
sin_x = math.sin(x) # trigonometric functions will return values in radians by default
print(sin_x)
print(math.sin(math.pi))

sin_180 = math.floor(math.sin(math.pi)) # pi = 180 in radians
print(sin_180)


print('\ninverse functions of trigonometry')
sinInv_0 = math.asin(0)
print(sinInv_0)
cosInv_0 = math.acos(0)
print(cosInv_0)


print('\nright triangle')
base = 3
parpendicular = 4
hypotenous = math.hypot(base, parpendicular)
print(hypotenous)


print('\nlog and antilog/exponent :')
squr_of_9 =math.pow(9,2)
print(squr_of_9)

exponent_1 = math.e
print(exponent_1)

log_exp_1 = math.log(exponent_1)
print(log_exp_1)

exponent_2 = math.exp(2)
print(exponent_2)

log_exp_2 = math.log(exponent_2)
print(log_exp_2)

print('\nlog bases 10 & 2:')
log10_1000 = math.log10(1000)
print(log10_1000)

log2_16 = math.log2(16)
print(log2_16)