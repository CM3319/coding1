def positiveOrNegativenumber():
    if number > -1:
        print('this is a postive number')
    elif number < 0:
        print('This is a negative number')
    elif number == 0:
        print('this is zero.')
    else:
        print('number not recognized')

        positiveOrnegative(-1)


        def shoppingdiscount(membership, itemname, itemprice):
            if membership == 'superShopper':
                print('you will get 10 percent off your item')
                discountAmount = Itemprice * 0.1
                FinalAmount = itemPrice -discountAmount
                print(finalAmount)
            elif membership== 'megaShopper':
                discountAmount = Itemprice * 0.15
                FinalAmount = itemPrice -discountAmount
                print(finalAmount)
                print('you will get 15 percent off your item')
            elif membership=='ultraShopper':
                discountAmount = Itemprice * 0.2
                FinalAmount = itemPrice -discountAmount
                print(finalAmount)
                print('you will get 20 percent off your item') 
            else:
                print('you do not have any membership benefits')

            shoppingDiscount('superShopper', 100, airfryer)    