# - https://docs.python.jp/3/library/string.html#format-string-syntax
# - https://docs.python.jp/3/library/string.html#formatspec
# - https://docs.python.jp/3/library/string.html#format-examples

print('{0}'.format('foo'))
# foo

print('{}'.format('foo'))
# foo

print('{}, {}, {}'.format('one', 'two', 'three'))
# one, two, three

print('{0}, {1}, {0}'.format('foo', 'bar'))
# foo, bar, foo

print('{word1}, {word2}, {word1}'.format(word1='one', word2='two'))
# one, two, one

person = {'name': 'ALice', 'age': 20}
print('{0[name]} is {0[age]} years old.'.format(person))
# ALice is 20 years old.

i = 100
print('left  : {:<10}'.format(i))
print('center: {:^10}'.format(i))
print('right : {:>10}'.format(i))
# left  : 100       
# center:    100    
# right :        100

i = 100
print('left  : {:*<10}'.format(i))
print('center: {:*^10}'.format(i))
print('right : {:*>10}'.format(i))
# left  : 100*******
# center: ***100****
# right : *******100

i = 255
print('bin: {:b}'.format(i))
print('oct: {:o}'.format(i))
print('dec: {:d}'.format(i))
print('hex: {:x}'.format(i))
# bin: 11111111
# oct: 377
# dec: 255
# hex: ff

i = 255
print('bin: {:0>8b}'.format(i))
print('oct: {:0>8o}'.format(i))
print('dec: {:0>8d}'.format(i))
print('hex: {:0>8x}'.format(i))
# bin: 11111111
# oct: 00000377
# dec: 00000255
# hex: 000000ff