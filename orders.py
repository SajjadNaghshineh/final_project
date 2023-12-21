import os
import csv
import pandas as pd
import datetime
from shops import Shops
from products import Products

"""
Orders class manages orders and its inheritance from Shops and Products is for when we change a 
field in customers file, the same field in orders and products must be change or sometimes we should
continiously update products.csv and shops.csv base on  orders.csv
"""

class Orders(Shops, Products):
    # Initialize the base data, if orders.csv exits we fill our data set by its file data,
    # else empty
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
        # Every time we create an instance of orders class, we set the bougth_count, available_count
        # in products.csv and also set the total_sell and unsend orders in shops.csv
        self.update_orders()
        self.update_products_count()
        self.update_shops_count()
        
    # You can just edit recieve_date and it automatically is today's date,
    # because other fields will be automatically updated
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
        shop_id = self.orders_data["shop_id"][idx]
        shop_id = self.shops_data["shop_id"].index(shop_id)
        x = int(self.shops_data["unsend_orders"][shop_id]) - 1
        self.shops_data["unsend_orders"][shop_id] = x
        
        self.update_shops()
        
    # This function continiously update our data set
    def update_orders(self):
        df = pd.DataFrame(self.orders_data)
        df.to_csv(self.orders_filepath, index=False)
        
    # We use this function to read data in a human readable way
    def read_orders(self):
        self.update_orders()
        df = pd.read_csv(self.orders_filepath)
        return df
    
    def update_products_count(self):
        # For each product that is in orders.csv, we set bought_count and available_count in products.csv
        for product in range(len(self.orders_data["product_id"])):
            qua = int(self.orders_data["quantity"][product])
            
            idx = self.products_data["product_id"].index(self.orders_data["product_id"][product])
            
            a = int(self.products_data["available_count"][idx]) - qua
            self.products_data["available_count"][idx] = a
            
            b = int(self.products_data["bought_count"][idx]) + qua
            self.products_data["bought_count"][idx] = b
            
        self.update_products()
        
    def update_shops_count(self):
        # For each shop tahat is in orders.csv, we set unsend orders and total sell
        for id in range(len(self.orders_data["shop_id"])):
            rec = self.orders_data["recieve_date"][id]
            
            if rec == "nan":
                idx = self.shops_data["shop_id"].index(self.orders_data["shop_id"][id])
                x = int(self.shops_data["unsend_orders"][idx]) + 1
                self.shops_data["unsend_orders"][idx] = x
                
        for i in range(len(self.orders_data["shop_id"])):
            proid = self.orders_data["product_id"][i]
            qua = float(self.orders_data["quantity"][i])
            
            idx = self.products_data["product_id"].index(proid)
            price = float(self.products_data["price"][idx])
            
            total = price * qua
            
            idx = self.shops_data["shop_id"].index(self.orders_data["shop_id"][i])
            x = float(self.shops_data["total_sell"][idx]) + total
            self.shops_data["total_sell"][idx] = x
            
        self.update_shops()
        