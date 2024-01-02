# 코딩도장 p.165 심사문제


price=int(input())
coupon=input()

if coupon[4:] == "Cash" :
    print(price-int(coupon[4:]))