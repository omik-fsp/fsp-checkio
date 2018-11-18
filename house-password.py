def checkio(data: str) -> bool:
    
    upper = False
    lower = False
    digit = False
    
    if len(data) > 9:
        for char in data:
            if char.isupper():
                upper = True
            elif char.isdigit():
                digit = True
            elif char.islower():
                lower = True
    
    if upper and lower and digit:
        result = True
    else:
        result = False
