from distutils.util import strtobool

print(strtobool('true'))
print(strtobool('True'))
print(strtobool('TRUE'))
# 1
# 1
# 1

print(strtobool('t'))
print(strtobool('yes'))
print(strtobool('y'))
print(strtobool('on'))
print(strtobool('1'))
# 1
# 1
# 1
# 1
# 1

print(strtobool('false'))
print(strtobool('False'))
print(strtobool('FALSE'))
# 0
# 0
# 0

print(strtobool('f'))
print(strtobool('no'))
print(strtobool('n'))
print(strtobool('off'))
print(strtobool('0'))
# 0
# 0
# 0
# 0
# 0

print(type(strtobool('true')))
# <class 'int'>
