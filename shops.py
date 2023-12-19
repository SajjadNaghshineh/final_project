import os
import csv
import pandas as pd
from random import randint

class CentralShop:
    pass

class Shops:
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
                
    def add_shop(self):
        for i in self.shops_header:
            if i == "shop_id":
                sh_id = randint(11111, 99999)
                while True:
                    if sh_id not in self.shops_data[i]:
                        self.shops_data[i].append(sh_id)
                        break
            elif i == "shop_name":
                name = input(f"Enter the {i}: ")
                self.shops_data[i].append(name)
            else:
                self.shops_data[i].append(0)
                
        self.update_shops()
        
    def edit_shop(self):
        counter = 0
        while True:
            if counter == 0:
                print("You can just change shop name, other fields will be automatically filled.")
            shopid = input("Enter the shop id: ")
            if int(shopid) in self.shops_data["shop_id"] or shopid in self.shops_data["shop_id"]:
                break
            else:
                print(f"This shop id: {shopid} is not available, try again ...")
                counter += 1
                
        value = input("Enter new name: ")
        
        try:
            idx = self.shops_data["shop_id"].index(int(shopid))
        except:
            idx = self.shops_data["shop_id"].index(shopid)
            
        self.shops_data["shop_name"][idx] = value
        
        self.update_shops()
        
    def update_shops(self):
        df = pd.DataFrame(self.shops_data)
        df.to_csv(self.shops_filepath, index=False)
        
    def read_shops(self):
        self.update_shops()
        df = pd.read_csv(self.shops_filepath)
        return df
    