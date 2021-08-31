mango = 15
apple = 20
lichi = 60
user_name = input("Please enter your name: ")
buffer_bucket = []
price_bucket = []
juice_bucket = []
billing_list = []
print ("Welcome to Manoj Juice Bar")
print (" Enter 1 for Apple \n Enter 2 for Mango \n Enter 3 for Lichi\n Enter 4 to final the order\n")

while True:
    user_item = int(input("Enter your Choice: "))
    if user_item != 4:
        buffer_bucket.append(user_item)
        user_quantity = int(input("Enter Quantity: "))
        price_bucket.append(user_quantity)
        continue
    else:
        print ("Finalizing your Bill\n")
        break
print ("Proceeding for preparation.......\n")
#print (buffer_bucket)
#print (price_bucket)

for i in buffer_bucket:
    if i == 1:
        juice_bucket.append(apple)
    if i == 2:
        juice_bucket.append(mango)
    if i == 3:
        juice_bucket.append(lichi)
#print (juice_bucket)        
    
for i in range(len(juice_bucket)):
    billing_list.append(juice_bucket[i] * price_bucket[i])
    
Final_price = sum(billing_list)
#print(Final_price)

print (f"{user_name} your total Billed amount is {Final_price} Rupess") 
