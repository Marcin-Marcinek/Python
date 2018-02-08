#!/usr/bin/python3
print("TVA Calculator")
Price = float(input("What is the price of the product?"))
TVA = float(input("What is the TVA of the product?"))
finalPrice = Price + Price * TVA/100
print('the final price of the product after taxes is: ', finalPrice)