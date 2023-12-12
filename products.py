from file_manager import FileManager

class Products(FileManager):
    fieldnames = ["product_id", "product_name", "company_name", "production_date", "expiration_period", "bought_count", "available_count", "price"]
    filepath = "products.csv"
    
    # first of all we create products.csv file
    def __init__(self):
        self.create_file(self.filepath, self.fieldnames)
        
    # read data from products.csv file
    def read_products_csv(self):
        self.df = self.read_file(self.filepath)
        return self.df
    
    # append data to products.csv file
    def append_products_csv(self):
        self.append_data(self.filepath, self.fieldnames, "product_id")
        
    # change products.csv data
    def change_products_csv(self):
        self.change_data(self.filepath, self.fieldnames, "product_id")
        