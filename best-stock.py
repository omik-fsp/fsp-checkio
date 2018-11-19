def best_stock(data):
    # your code here
    x = 0

    for i in data:
        if data[i] > x:
            x = data[i]
            result = i

    return result


print("Example:")
print(best_stock({'CAC': 10.0, 'ATX': 390.2, 'WIG': 1.2}))
