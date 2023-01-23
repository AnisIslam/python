def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x-1)

print("Typr a value: ")
value = int(input())
print(factorial(value))
