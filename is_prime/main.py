# check the number, if is prime, return True, else return False;

def is_prime(number):
    for i in range(2, number):
        if (number % i) == 0:
            return False
        return True

print(is_prime(2))
print(is_prime(8))
print(is_prime(23))
