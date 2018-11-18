# 1. on CheckiO your solution should be a function
# 2. the function should return the right answer, not print it.

def say_hi(name: str, age: int) -> str:
    
    return 'Hi. My name is {0} and I\'m {1} years old'.format(name, age)


print(say_hi("Alex", 32))
print(say_hi("Frank", 68))
