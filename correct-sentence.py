def correct_sentence(text: str) -> str:
    """
        returns a corrected sentence which starts with a capital letter
        and ends with a dot.
    """
    # your code here

    return text[:1].upper() + text[1:] + '.' if not text.endswith('.') else text[:1].upper() + text[1:]


print("Example:")
print(correct_sentence("Welcome to New York."))
