import re

def first_word(text: str) -> str:
    """
        returns the first word in a given text.
    """
    # your code here
    
    text = re.sub(r"[^\w']+", ' ', text)
    
    return text.split()[0]



print("Example:")
print(first_word("...a word..."))
print(first_word("don't touch it"))
print(first_word("greetings, friends"))