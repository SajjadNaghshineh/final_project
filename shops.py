import os
import csv
import pandas as pd
from random import randint

# Shops class mangages shops
class Shops:
    # Initialize the base data, if shops.csv exits we fill our data set by its file data,
    # else empty
    shops_header = ["shop_id", "shop_name", "unsend_orders", "total_sell"]
    shops_filepath = "shops.csv"
    
    shops_data = {
        "shop_id": [],
        "shop_name": [],
        "unsend_orders": [],
        "total_sell": []
    }
    
    if os.path.exists(shops_filepath):
        with open(shops_filepath, "r") as csvfile:
            reader = csv.reader(csvfile)
            next(reader)
            
            for row in reader:
                shops_data["shop_id"].append(row[0])
                shops_data["shop_name"].append(row[1])
                shops_data["unsend_orders"].append(row[2])
                shops_data["total_sell"].append(row[3])
                
    def __init__(self):
        # Every time we create an instance of shops class, we update our data set
        self.update_shops()
        
    def add_shop(self):
        for i in self.shops_header:
            if i == "shop_id":
                sh_id = randint(11111, 99999)
                # we set a unique id for each shop
                while True:
                    if sh_id not in self.shops_data[i]:
                        self.shops_data[i].append(sh_id)
                        break
            elif i == "shop_name":
                # If this shop already registered it raise an error and remove the generated id
                name = input(f"Enter the {i}: ")
                if name not in self.shops_data["shop_name"]:
                    self.shops_data[i].append(name)
                else:
                    self.shops_data["shop_id"].remove(sh_id)
                    raise ValueError(f"This shop: {name} is already exists.")
            else:
                self.shops_data[i].append(0)
                
        self.update_shops()
        
    def edit_shop(self):
        # Edit shops data can be done base on unique field shop_id, 
        # also you can just edit shop name, because other fields will be automatically updated
        counter = 0
        while True:
            # If the entered shop_id isn't in shop_id, its alarm
            if counter == 0:
                print("You can just change shop name, other fields will be automatically filled.")
            shopid = input("Enter the shop id: ")
            if int(shopid) in self.shops_data["shop_id"] or shopid in self.shops_data["shop_id"]:
                break
            else:
                print(f"This shop id: {shopid} is not available, try again ...")
                counter += 1
                
        value = input("Enter new name: ")
        
        # When we first add shop_id, its value is int and when we read data from file its str, so ...
        try:
            idx = self.shops_data["shop_id"].index(int(shopid))
        except:
            idx = self.shops_data["shop_id"].index(shopid)
            
        self.shops_data["shop_name"][idx] = value
        
        self.update_shops()
        
    # This function continiously update our data set
    def update_shops(self):
        df = pd.DataFrame(self.shops_data)
        df.to_csv(self.shops_filepath, index=False)
        
    # We use this function to read data in a human readable way
    def read_shops(self):
        self.update_shops()
        df = pd.read_csv(self.shops_filepath)
        return df
    