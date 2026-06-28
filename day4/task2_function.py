def a_discount(price,per=10):
    discount=price*per/100
    f_price=price-discount
    return f_price
print("price after discount:",a_discount(4500))
print("price after 20% discount:",a_discount(6500,per=20))