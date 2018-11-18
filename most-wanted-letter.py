from collections import Counter


def checkio(text: str) -> str:

    # Strip all but letters
    text = ''.join(filter(str.isalpha, text))

    # Casefolding!
    text = text.casefold()

    # Count most common letters
    result = Counter(text).most_common()

    # Sort em!
    result.sort(key=lambda x: (-x[1], x[0]))

    return result[0][0]


print("Example:")
print(checkio("Hello World!"))
