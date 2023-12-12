from file_manager import FileManager

class Customers(FileManager):
    fieldnames = ["username", "fullname", "user_id", "phone", "total_price", "sale_amount", "unpaid_amount"]
    filepath = "customers.csv"
    
    # first of all we create customers.csv file
    def __init__(self):
        self.create_file(self.filepath, self.fieldnames)
        
    # read data from customers.csv file
    def read_customers_csv(self):
        self.df = self.read_file(self.filepath)
        return self.df
    
    # append data to customers.csv file
    def append_customers_csv(self):
        self.append_data(self.filepath, self.fieldnames, "user_id")
        
    # change customers.csv data
    def change_customers_csv(self):
        self.change_data(self.filepath, self.fieldnames, "user_id")
        