def between_markers(text: str, begin: str, end: str) -> str:
    """
        returns substring between two given markers
    """
    # your code here

    beginPos = text.find(begin)
    endPos = text.find(end)

    if beginPos == -1:
        beginPos = 0
    else:
        beginPos = beginPos + len(begin)

    if endPos == -1:
        endPos = len(text)

    result = text[beginPos:endPos]

    return result


print('Example:')
print(between_markers('<head><title>My new site</title></head>', '<title>', '</title>'))
