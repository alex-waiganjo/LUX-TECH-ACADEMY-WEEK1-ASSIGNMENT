def prime_number():
    num = int(input("Enter  any  number:  "))
    if num % 2 == 0:
        print(f' Number {num} is not a  Prime Number')
    else:
        print(f' Number {num}  is  a  Prime Number')


prime_number()