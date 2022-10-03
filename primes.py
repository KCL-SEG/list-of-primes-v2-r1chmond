"""List of prime numbers generator."""

def primes(number_of_primes):
    if number_of_primes < 1:
        raise ValueError(f"Enter a value which is greater than 0")
    list = []
    for i in range(2, 9223372036854775807):
        if isPrime(i):
            list.append(i)
        if len(list) == number_of_primes:
            break
    return list

#check if a number is prime
def isPrime(num):
    if num == 2 or num == 3:
        return True
    elif num % 2 == 0 or num < 2 or num % 3 == 0:
        return False
    else:
        for element in range(5, int((num ** (1/2))+1), 2):
            if num % element == 0:
                return False
    return True