def prime_checker(number):
    divisor = 2
    is_prime = True
    while is_prime and divisor < number:
        if number % divisor == 0:
            is_prime = False
        divisor += 1

    # is_prime = True
    # for divisor in range(2, number):
    #     if number % divisor == 0:
    #         is_prime = False
    # if is_prime:
    #     print("It's a prime number.")
    # else:
    #     print("It's not a prime number.")

    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")
        
        
n = int(input("Check this number: "))
prime_checker(number=n)
