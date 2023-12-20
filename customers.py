import os
import csv
import pandas as pd
from orders import Orders
from products import Products

class Customers(Orders, Products):
    customers_header = ["username", "fullname", "user_id", "phone", "total_buy", "paid_amount", "unpaid_amount", "credit", "discount"]
    customers_filepath = "customers.csv"
    
    customers_data = {
        "username": [],
        "fullname": [],
        "user_id": [],
        "phone": [],
        "total_buy": [],
        "paid_amount": [],
        "unpaid_amount": [],
        "credit": [],
        "discount": []
    }
    
    if os.path.exists(customers_filepath):
        with open(customers_filepath, "r") as csvfile:
            reader = csv.reader(csvfile)
            next(reader)
            
            for row in reader:
                customers_data["username"].append(row[0])
                customers_data["fullname"].append(row[1])
                customers_data["user_id"].append(row[2])
                customers_data["phone"].append(row[3])
                customers_data["total_buy"].append(row[4])
                customers_data["paid_amount"].append(row[5])
                customers_data["unpaid_amount"].append(row[6])
                customers_data["credit"].append(row[7])
                customers_data["discount"].append(row[8])
                
    def __init__(self):
        self.check_customers_payment()
        
    def add_customer(self):
        for i in self.customers_header:
            if i == "username" or i == "user_id" or i == "phone":
                while True:
                    field = input(f"Enter a {i}: ")
                    if field not in self.customers_data[i]:
                        self.customers_data[i].append(field)
                        break
                    else:
                        print(f"This {i}: {field} is already exists, try another one ...")
            elif i == "fullname":
                full_name = input(f"Enter your {i}: ")
                self.customers_data[i].append(full_name)
            else:
                self.customers_data[i].append(0)
                
        self.update_customers()
        
    def edit_customer(self):
        while True:
            column = input(f"What column you want to change? {self.customers_header}: ")
            if column in ["total_buy", "discount", "paid_amount", "unpaid_amount", "credit"]:
                print(f"You are not allowed to change {column}, this value will be automatically updated")
            else:
                break
            
        while True:
            unique_field = input("Enter a unique value from these columns, username or user_id, phone: ")
            
            if unique_field in self.customers_data["username"] or unique_field in self.customers_data["user_id"] or unique_field in self.customers_data["phone"]:
                break
            else:
                print(f"Could not find any user with these value: {unique_field}")
                
        while True:
            value = input("Enter the new value: ")
            if column == "username":
                if value not in self.customers_data["username"]:
                    break
                else:
                    print(f"This {column}: {value} is already exists, try another one ...")
                    continue
            elif column == "user_id":
                if value not in self.customers_data["user_id"]:
                    break
                else:
                    print(f"This {column}: {value} is already exists, try another one ...")
                    continue
            elif column == "phone":
                if value not in self.customers_data["phone"]:
                    break
                else:
                    print(f"This {column}: {value} is already exists, try another one ...")
                    continue
            elif column == "fullname":
                break
            
        if unique_field in self.customers_data["username"]:
            idx = self.customers_data["username"].index(unique_field)
            self.customers_data[column][idx] = value
        elif unique_field in self.customers_data["user_id"]:
            idx = self.customers_data["user_id"].index(unique_field)
            self.customers_data[column][idx] = value
        elif unique_field in self.customers_data["phone"]:
            idx = self.customers_data["phone"].index(unique_field)
            self.customers_data[column][idx] = value
            
        self.update_customers()
        
        # if username changed here, it must be changed in orders
        if column == "username":
            old_value = self.customers_data["username"][idx]
            
            for i in range(len(self.orders_data["username"])):
                if i == old_value:
                    self.orders_data["username"][i] = value
            else:
                self.update_orders()
                
    def update_customers(self):
        df = pd.DataFrame(self.customers_data)
        df.to_csv(self.customers_filepath, index=False)
        
    def read_customers(self):
        self.update_customers()
        df = pd.read_csv(self.customers_filepath)
        return df
    
    def check_customers_payment(self):
        df_products = self.read_products()
        df_orders = self.read_orders()
        
        for name in self.customers_data["username"]:
            ids = df_orders[df_orders["username"] == name]["product_id"].values
            qua = df_orders[df_orders["username"] == name]["quantity"].values
            
            if len(ids) != 0 and len(qua) != 0:
                total = 0
                for i in range(len(ids)):
                    product_price = df_products[df_products["product_id"] == ids[i]]["price"].values[0]
                    product_price = float(product_price) * float(qua[i])
                    
                    total += product_price
                    
                user_idx = self.customers_data["username"].index(name)
                self.customers_data["total_buy"][user_idx] = total
                
                if float(self.customers_data["paid_amount"][user_idx]) == 0:
                    self.customers_data["unpaid_amount"][user_idx] = total
                else:
                    unpaid = float(total) - float(self.customers_data["paid_amount"][user_idx])
                    self.customers_data["unpaid_amount"][user_idx] = unpaid
                    
                last_id = ids[-1]
                last_qua = qua[-1]
                
                last_order_price = df_products[df_products["product_id"] == last_id]["price"].values[0]
                last_order_price = float(last_order_price) * float(last_qua)
                
                if self.customers_data["credit"][user_idx] == 0:
                    credit = float(total) // 500000 * 50000
                    self.customers_data["credit"][user_idx] = credit
                    
                if self.customers_data["discount"][user_idx] == 0:
                    discount = last_order_price // 100000 * 5
                    self.customers_data["discount"][user_idx] = discount
            
        self.update_customers()
        
    def customers_club(self):
        self.check_customers_payment()
        df_customers = self.read_customers()
        df_products = self.read_products()
        df_orders = self.read_orders()
        
        user_name = input("Enter your username: ")
        if user_name not in self.customers_data["username"]:
            raise ValueError(f"User not found by this username: {user_name}")
        
        if user_name not in self.orders_data["username"]:
            raise ValueError(f"This user: {user_name} hasn't bought anything yet.")
        
        idx = self.customers_data["username"].index(user_name)
        user_discount = df_customers[df_customers["username"] == user_name]["discount"].values[0]
        user_credit = df_customers[df_customers["username"] == user_name]["credit"].values[0]
        unpaid_amount = df_customers[df_customers["username"] == user_name]["unpaid_amount"].values[0]
        
        last_id = df_orders[df_orders["username"] == user_name]["product_id"].values[-1]
        last_qua = df_orders[df_orders["username"] == user_name]["quantity"].values[-1]
        
        last_order_price = df_products[df_products["product_id"] == last_id]["price"].values[0]
        last_order_price = float(last_order_price) * float(last_qua)
        
        if float(self.customers_data["unpaid_amount"][idx]) == 0:
            question = input("Which option you want to use, credit or discount? ")
            
            if question == "credit":
                if last_order_price < float(user_credit):
                    print("You can't use your credit because it is greater than your order price.")
                elif user_credit == 0:
                    print("Your credit is finished.")
                else:
                    x = last_order_price - float(user_credit)
                    y = float(self.customers_data["paid_amount"][idx]) + x
                    self.customers_data["paid_amount"][idx] = y
                    z = float(self.customers_data["unpaid_amount"][idx]) - x
                    self.customers_data["unpaid_amount"][idx] = z
                    
                    self.customers_data["credit"][idx] = 0
            else:
                if user_discount == 0:
                    print("You have no discount right now.")
                else:
                    discount = float(user_discount) * float(last_order_price) / 100
                    result_price = float(last_order_price) - discount
                    
                    y = float(self.customers_data["paid_amount"][idx]) + result_price
                    self.customers_data["paid_amount"] = y

                    self.customers_data["discount"] = 0
        else:
            if user_credit != 0:
                print("You can't use credit pay becaue you have unpaid amount.")
            if user_discount == 0:
                print("You have no discount right now.")
            else:
                discount = float(user_discount) * float(unpaid_amount) / 100
                result_price = float(unpaid_amount) - discount
                
                y = float(self.customers_data["paid_amount"][idx]) + result_price
                self.customers_data["paid_amount"][idx] = y
                z = float(self.customers_data["unpaid_amount"][idx]) - result_price
                self.customers_data["unpaid_amount"][idx] = z
                
                self.customers_data["discount"][idx] = 0

        self.update_customers()
        