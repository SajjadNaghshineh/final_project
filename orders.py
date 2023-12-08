import os
import csv
import pandas as pd

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
        self.values = []
        for i in self.fieldnames:
            self.question = input(f"Enter the {i}: ")
            self.values.append(self.question)
            
        # if guard clause technique
        if not os.path.exists("orders.csv"):
            self.create_orders_csv()
            
        with open("orders.csv", "a", newline='') as csvfile:
            self.writer = csv.DictWriter(csvfile, fieldnames=self.fieldnames)
            self.writer.writerow({
                self.fieldnames[0]: self.values[0],
                self.fieldnames[1]: self.values[1],
                self.fieldnames[2]: self.values[2],
                self.fieldnames[3]: self.values[3],
                self.fieldnames[4]: self.values[4],
                self.fieldnames[5]: self.values[5],
                self.fieldnames[6]: self.values[6],
            })
    
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
                