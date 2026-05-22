def Prime_or_Not(num):
    if num < 2:
        return False
    elif num >= 2:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

print(Prime_or_Not(36))
# print('Hello')
