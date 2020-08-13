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
