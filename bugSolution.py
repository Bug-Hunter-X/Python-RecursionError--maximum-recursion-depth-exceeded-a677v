def function(x):
    result = 0
    for i in range(1, x + 1):
        result += i
    return result

print(function(5)) #This will work correctly even for large numbers
