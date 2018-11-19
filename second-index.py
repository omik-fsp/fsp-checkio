def second_index(text: str, symbol: str) -> [int, None]:
    """
        returns the second index of a symbol in a given text
    """
    # your code here

    firstOcurrence = text.find(symbol)
    result = text.find(symbol, firstOcurrence + 1)

    if result == -1:
        result = None


    return result


print('Example:')
print(second_index("hi peter parker porting potatoes", "p"))
