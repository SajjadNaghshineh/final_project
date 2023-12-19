import os
import csv
import pandas as pd
from random import randint

class Products:
    products_header = ["product_id", "product_name", "company_name", "production_date", "expiration_period", "bought_count", "available_count", "price"]
    products_filepath = "products.csv"
    
    products_data = {
        "product_id": [],
        "product_name": [],
        "company_name": [],
        "production_date": [],
        "expiration_period": [],
        "bought_count": [],
        "available_count": [],
        "price": []
    }
        
    if os.path.exists(products_filepath):
        with open(products_filepath, "r") as csvfile:
            reader = csv.reader(csvfile)
            next(reader)
                
            for row in reader:
                products_data["product_id"].append(row[0])
                products_data["product_name"].append(row[1])
                products_data["company_name"].append(row[2])
                products_data["production_date"].append(row[3])
                products_data["expiration_period"].append(row[4])
                products_data["bought_count"].append(row[5])
                products_data["available_count"].append(row[6])
                products_data["price"].append(row[7])
                
    def add_product(self):
        for i in self.products_header:
            if i == "product_id":
                pro_id = randint(11111, 99999)
                while True:
                    if pro_id not in self.products_data[i]:
                        self.products_data[i].append(pro_id)
                        break
            elif i == "bought_count":
                self.products_data[i].append(0)
            else:
                field = input(f"Enter value for {i}: ")
                self.products_data[i].append(field)
            
        self.update_products()
        
    def edit_product(self):
        while True:
            column = input(f"What column you want to change? {self.products_header}: ")
            if column == "product_id":
                print("You are not allowed to change product id field!!!")
            else:
                break
            
        while True:
            id = input("Enter the product id: ")
            if int(id) in self.products_data["product_id"] or id in self.products_data["product_id"]:
                break
            else:
                print(f"This product id: {id} is not available, try again ...")
            
        value = input("Enter the new value: ")
        
        try:
            idx = self.products_data["product_id"].index(int(id))
        except:
            idx = self.products_data["product_id"].index(id)
            
        self.products_data[column][idx] = value
        
        self.update_products()
        
    def update_products(self):
        df = pd.DataFrame(self.products_data)
        df.to_csv(self.products_filepath, index=False)
        
    def read_products(self):
        self.update_products()
        df = pd.read_csv(self.products_filepath)
        return df
    