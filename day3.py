
number = int(input("Enter your number"))

prime_check = True

if number <= 1:
    prime_check = False
else:
    for i in range(2, int(number**0.5)+ 1):
        if number % i == 0:
            prime_check = False
            break



if(number % 2):
    print(f"Yes,{number} is a prime number.")
else:    
    print(f"No,{number} is not a prime number.")