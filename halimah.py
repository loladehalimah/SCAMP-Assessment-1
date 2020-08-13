
# nterms = int(input("How many terms? "))

# # first two terms
# n1, n2 = 0, 1
# count = 0

# # check if the number of terms is valid
# if nterms <= 0:
#    print("Please enter a positive integer")
# elif nterms == 1:
#    print("Fibonacci sequence upto",nterms,":")
#    print(n1)
# else:
#    print("Fibonacci sequence:")
#    while count < nterms:
#        print(n1)
#        nth = n1 + n2
#        # update values
#        n1 = n2
#        n2 = nth
#        count += 1

def fibo(number):
    num = int(number)
    count = 0
    start_0, start_1 = 0,1

    if num <= 0:
        print('Number must be greater than zero')
    elif num == 1:
        print('Fibbonacci up to {0} term'.format(start_0))
        print(start_0)
    else:
        print('Fibbonacci....')
        while count < num :
            print(start_0)
            nth = start_0 + start_1

            start_0 = start_1
            start_1 = nth

            count +=1

fibo(7)