import os
import csv
import pandas as pd
from orders import Orders

class Customers(Orders):
    customers_header = ["username", "fullname", "user_id", "phone", "total_price", "sale_amount", "unpaid_amount"]
    customers_filepath = "customers.csv"
    
    customers_data = {
        "username": [],
        "fullname": [],
        "user_id": [],
        "phone": [],
        "total_price": [],
        "sale_amount": [],
        "unpaid_amount": []
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
                customers_data["total_price"].append(row[4])
                customers_data["sale_amount"].append(row[5])
                customers_data["unpaid_amount"].append(row[6])
                
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
            if column in ["total_price", "sale_amount", "unpaid_amount"]:
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
    