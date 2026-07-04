#lista de primos
def ePrimo(n):
    if n == 2:
        return True
    
    elif n < 2 or n % 2 == 0:
        return False
        
    for num in range(3, n, 2):
        if n % num == 0:
            return False
        
    return True

ate = int(input())
primos = [primo for primo in range(1, ate + 1) if ePrimo(primo)]
print(primos)