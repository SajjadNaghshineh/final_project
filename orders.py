from file_manager import FileManager

class CustomerOrders:
    pass

class ShopOrders:
    pass

class TotalOrders(FileManager):
    fieldnames = ["order_id", "username", "shop_id", "product_id", "quantity", "order_date", "recieve_date"]
    filepath = "orders.csv"
    
    # first of all we create orders.csv file
    def __init__(self):
        self.create_file(self.filepath, self.fieldnames)
        
    # read data from orders.csv file
    def read_orders_csv(self):
        self.df = self.read_file(self.filepath)
        return self.df
    
    # append data to orders.csv file
    def append_orders_csv(self):
        self.append_data(self.filepath, self.fieldnames, "order_id")
        
    # change orders.csv data
    def change_orders_csv(self):
        self.change_data(self.filepath, self.fieldnames, "order_id")
        