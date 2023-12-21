import os
os.system("cls")
from products import Products
from customers import Customers
from orders import Orders
from shops import Shops

"""
In this program we use lists to easily change add data, change data, remove and retrieve data.
In this way when we inherits classes, we can easilly change our data.
"""

print("The list of actions you can do:")
print("1. Register a user")
print("2. Change a user's data")
print("3. Register a shop")
print("4. Change a shop's data")
print("5. Add a product")
print("6. Change a product's data")
print("7. Enter the deliver order")
print("8. Analyse customers club")
print()
print("Enter whatever except 1 to 8 to finish the program.")
print()

counter = 0
while True:
    counter += 1
    
    try:
        if counter == 1:
            products_obj = Products()
            customers_obj = Customers()
            orders_obj = Orders()
            shops_obj = Shops()
            
        question = input("Please enter the number of action from above: ")
        
        match question:
            case "1":
                print(customers_obj.read_customers())
                customers_obj.add_customer()
                print(customers_obj.read_customers())
                print("User registration is done.")
            case "2":
                print(customers_obj.read_customers())
                customers_obj.edit_customer()
                print(customers_obj.read_customers())
                print("User edition is done.")
            case "3":
                print(shops_obj.read_shops())
                shops_obj.add_shop()
                print(shops_obj.read_shops())
                print("Shop registration is doen.")
            case "4":
                print(shops_obj.read_shops())
                shops_obj.edit_shop()
                print(shops_obj.read_shops())
                print("Shop edition is done.")
            case "5":
                print(products_obj.read_products())
                products_obj.add_product()
                print(products_obj.read_products())
                print("Product is added successfully.")
            case "6":
                print(products_obj.read_products())
                products_obj.edit_product()
                print(products_obj.read_products())
                print("Product edited successfully.")
            case "7":
                print(orders_obj.read_orders())
                orders_obj.edit_order()
                print(orders_obj.read_orders())
                print("Order delivery is entered.")
            case "8":
                print(customers_obj.read_customers())
                customers_obj.customers_club()
                print(customers_obj.read_customers())
                print("User discount used successfully.")
            case _:
                break
    except Exception as e:
        print(f"Error: {e}")
        continue
    
    print("-" * 30)
    
print("Program finished.")
