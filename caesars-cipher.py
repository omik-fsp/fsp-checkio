def to_encrypt(text, delta):


    output = ''

    for char in text:
        
        # Storing current char Number
        charN = ord(char)

        # Lets add (delta) to char Number each loop 
        if charN >= 97:
            charN += delta

        # If over 122 or under 97 add or substract 26 to keep at same (delta) distance
        if charN > 122:
            charN -= 26

        if charN < 97 and charN != 32:
            charN += 26

        output += chr(charN)

    return output
