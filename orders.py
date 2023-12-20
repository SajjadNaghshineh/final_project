import os
import csv
import pandas as pd
import datetime
from shops import Shops

class Orders(Shops):
    orders_header = ["order_id", "username", "shop_id", "product_id", "quantity", "order_date", "recieve_date"]
    orders_filepath = "orders.csv"
    
    orders_data = {
        "order_id": [],
        "username": [],
        "shop_id": [],
        "product_id": [],
        "quantity": [],
        "order_date": [],
        "recieve_date": []
    }
    
    if os.path.exists(orders_filepath):
        with open(orders_filepath, "r") as csvfile:
            reader = csv.reader(csvfile)
            next(reader)
            
            for row in reader:
                orders_data["order_id"].append(row[0])
                orders_data["username"].append(row[1])
                orders_data["shop_id"].append(row[2])
                orders_data["product_id"].append(row[3])
                orders_data["quantity"].append(row[4])
                orders_data["order_date"].append(row[5])
                orders_data["recieve_date"].append(row[6])
                
    def __init__(self):
        self.update_orders()
        
    def edit_order(self):
        while True:
            orderid = input("Enter the order id: ")
            if orderid not in self.orders_data["order_id"]:
                print(f"This order id: {orderid} is not available, try again ...")
            else:
                break
            
        today = datetime.date.today()
        
        idx = self.orders_data["order_id"].index(orderid)
        self.orders_data["recieve_date"][idx] = today
        
        self.update_orders()
        
        # when we set recieve date, unsend_orders in orders must be minus one
        shop_id = int(self.orders_data["shop_id"][idx])
        self.shops_data["unsend_orders"][shop_id] -= 1
        
        self.update_shops()
        
    def update_orders(self):
        df = pd.DataFrame(self.orders_data)
        df.to_csv(self.orders_filepath, index=False)
        
    def read_orders(self):
        self.update_orders()
        df = pd.read_csv(self.orders_filepath)
        return df
    