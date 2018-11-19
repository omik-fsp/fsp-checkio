# Your optional code here
# You can import some modules or create additional functions


def checkio(data: list) -> list:
    # Your code here
    # It's main function. Don't remove this function
    # It's used for auto-testing and must return a result for check.

    result = []

    for x in data:
        z = data.count(x)

        if data.count(x) > 1:
            result.append(x)

    # replace this for solution
    return result


# Some hints
# You can use list.count(element) method for counting.
# Create new list with non-unique elements
# Loop over original list
print(checkio([1, 2, 3, 1, 3]))
# These "asserts" using only for self-checking and not necessary for auto-testing
