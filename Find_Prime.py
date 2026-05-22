def Prime_or_Not(num):
    if num < 2:
        return False
    elif num >= 2:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

print(Prime_or_Not(2))
# print('Hello')
