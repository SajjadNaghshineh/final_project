import os
import csv
import pandas as pd
from random import randint

class Orders:
    fieldnames = ["order_id", "customer_name", "shop_id", "product_id", "quantity", "order_date", "recieve_date"]
    
    def __init__(self):
        self.create_orders_csv()
    
    # create csv file
    def create_orders_csv(self):
        if not os.path.exists("orders.csv"):
            with open("orders.csv", "w", newline='') as csvfile:
                self.writer = csv.DictWriter(csvfile, fieldnames=self.fieldnames)
                self.writer.writeheader()
                
    # read data from csv file
    def read_orders_csv(self):
        # if guard clause technique
        if not os.path.exists("orders.csv"):
            self.create_orders_csv()
            
        self.df = pd.read_csv("orders.csv")
        return self.df
    
    # append data to csv file
    def append_orders_data(self):    
        # if guard clause technique
        if not os.path.exists("orders.csv"):
            self.create_orders_csv()
            
        self.df = pd.read_csv("orders.csv")
        self.df_ids = self.df["order_id"].values
        
        while True:
            self.id = randint(1111, 9999)
            if self.id not in self.df_ids:
                break
        
        self.values = [str(self.id)]
        
        for i in range(1, len(self.fieldnames)):
            self.question = input(f"Enter the {self.fieldnames[i]}: ")
            self.values.append(self.question)
            
        with open("orders.csv", "a", newline='') as csvfile:
            self.writer = csv.DictWriter(csvfile, fieldnames=self.fieldnames)
            self.writer.writerow(dict(zip(self.fieldnames, self.values)))
            
    # change orders data
    def change_orders_data(self):
        self.question1 = input("Enter the order id : ")
        self.question2 = input(f"What column you want to change, {self.fieldnames}: ")
        self.question3 = input("Enter new value: ")
        
        # if guard clause technique
        if not os.path.exists("orders.csv"):
            self.create_orders_csv()
            
        with open("orders.csv", "r") as csvfile:
            self.reader = csv.DictReader(csvfile)
            self.rows = list(self.reader)
            
        with open("orders.csv", "w", newline='') as csvfile:
            self.writer = csv.DictWriter(csvfile, fieldnames=self.fieldnames)
            self.writer.writeheader()
            for row in self.rows:
                if row["order_id"] == self.question1:
                    row[self.question2] = self.question3
                self.writer.writerow(row)
                