def popular_words(text: str, words: list) -> dict:
    # your code here
    text = text.casefold().split()
    result = {}

    for x in words:
        x
        result[x] = text.count(x)

    return result


print("Example:")
print(popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was', 'three', 'near']))
