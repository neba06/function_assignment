'''Create a function named calculate_discount(price, discount_percent) 
that calculates the final price after applying a discount. 
The function should take the original price (price) and 
the discount percentage (discount_percent) as parameters. 
If the discount is 20% or higher, apply the discount; otherwise, 
return the original price.'''

def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        final_price = (price*discount_percent) / 100
    else:
        final_price = price
    
    return final_price
    
'''Using the calculate_discount function, prompt the user to enter 
the original price of an item and the discount percentage. 
Print the final price after applying the discount, or if no discount was applied, 
print the original price.'''

price = int(input("Enter The price: "))
discount_percent = int(input("Enter The Discount Percentage: "))

print(f"The Final Price = {calculate_discount(price, discount_percent)}")
