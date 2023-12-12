import os
import csv
import pandas as pd
from random import randint

class FileManager:
    # create a specific file
    def create_file(self, filepath, fieldnames):
        # we use this if statment to avoid write header for multiple object instantiation
        if not os.path.exists(filepath):
            with open(filepath, "w", newline='') as csvfile:
                self.writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                self.writer.writeheader()
                
    # read data from a specific file
    def read_file(self, filepath):
        self.df = pd.read_csv(filepath)
        return self.df
    
    # append data to a specific file
    def append_data(self, filepath, fieldnames, unique_field):
        self.df = self.read_file(filepath)
        self.df_ids = self.df[unique_field].values
        
        while True:
            self.id = randint(11111111, 99999999)
            if self.id not in self.df_ids:
                break
            
        self.values = []
        
        for i in fieldnames:
            if i == unique_field:
                self.values.append(str(self.id))
                continue
            self.question = input(f"Enter value for {i}: ")
            self.values.append(self.question)
            
        with open(filepath, "a", newline='') as csvfile:
            self.writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            self.writer.writerow(dict(zip(fieldnames, self.values)))
            
    # change data from a specific file
    def change_data(self, filepath, fieldnames, unique_field):
        self.id_question = input(f"Enter the {unique_field}: ")
        self.column_question = input(f"What column you want to change, {fieldnames}: ")
        self.value_question = input("Enter new value: ")
        
        with open(filepath, "r") as csvfile:
            self.reader = csv.DictReader(csvfile)
            self.rows = list(self.reader)
            
        with open(filepath, "w", newline='') as csvfile:
            self.writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            self.writer.writeheader()
            for row in self.rows:
                if row[unique_field] == self.id_question:
                    row[self.column_question] = self.value_question
                self.writer.writerow(row)
                