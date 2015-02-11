def Euler3(n=600851475143):
    for i in range(2,100000):
        while n % i == 0:
            n //= i
            print((i))
            if n == 1 or n == i:
                return i
