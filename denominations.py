amount =int(input("Please Enter amount for withdraw:"))

bill_1=amount//100
bill_2=(amount%100)//50
bill_3=((amount%100)%50)//10

print("bills of 100 dollars", bill_1)
print("bills of 50 dollars", bill_2)
print("bills of 10 dollars", bill_3)