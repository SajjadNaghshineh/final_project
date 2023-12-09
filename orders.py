import os
import csv
import pandas as pd
from random import randint

class Orders:
    fieldnames = ["order_id", "customer_name", "shop_id", "product_id", "quantity", "order_date", "recieve_date"]
    filepath = "orders.csv"
    
    def __init__(self):
        self.create_orders_csv()
    
    # create csv file
    def create_orders_csv(self):
        # we use this if statment to avoid write header for multiple object instantiation
        if not os.path.exists(self.filepath):
            with open(self.filepath, "w", newline='') as csvfile:
                self.writer = csv.DictWriter(csvfile, fieldnames=self.fieldnames)
                self.writer.writeheader()
                
    # read data from csv file
    def read_orders_csv(self):
        self.df = pd.read_csv(self.filepath)
        return self.df
    
    # append data to csv file
    def append_orders_csv(self):
        self.df = self.read_orders_csv()
        self.df_ids = self.df["order_id"].values
        
        while True:
            self.id = randint(11111111, 99999999)
            if self.id not in self.df_ids:
                break
        
        self.values = [str(self.id)]
        
        for i in range(1, len(self.fieldnames)):
            self.question = input(f"Enter the {self.fieldnames[i]}: ")
            self.values.append(self.question)
            
        with open(self.filepath, "a", newline='') as csvfile:
            self.writer = csv.DictWriter(csvfile, fieldnames=self.fieldnames)
            self.writer.writerow(dict(zip(self.fieldnames, self.values)))
            
    # change orders data
    def change_orders_csv(self):
        self.id_question = input("Enter the order id : ")
        self.column_question = input(f"What column you want to change, {self.fieldnames}: ")
        self.value_question = input("Enter new value: ")
        
        with open(self.filepath, "r") as csvfile:
            self.reader = csv.DictReader(csvfile)
            self.rows = list(self.reader)
            
        with open(self.filepath, "w", newline='') as csvfile:
            self.writer = csv.DictWriter(csvfile, fieldnames=self.fieldnames)
            self.writer.writeheader()
            for row in self.rows:
                if row["order_id"] == self.id_question:
                    row[self.column_question] = self.value_question
                self.writer.writerow(row)
                