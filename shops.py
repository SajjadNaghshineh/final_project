from file_manager import FileManager

class CentralShop:
    pass

class SubsetShop(FileManager):
    fieldnames = ["shop_id", "shop_name", "unsend_orders", "total_sell"]
    filepath = "sub_shop.csv"
    
    # first of all we create sub_shop.csv file
    def __init__(self):
        self.create_file(self.filepath, self.fieldnames)
        
    # read data from sub_shop.csv file
    def read_sub_shop_csv(self):
        self.df = self.read_file(self.filepath)
        return self.df
    
    # append data to sub_shop.csv file
    def append_sub_shop_csv(self):
        self.append_data(self.filepath, self.fieldnames, "shop_id")
        
    # change sub_shop.csv data
    def change_sub_shop_csv(self):
        self.change_data(self.filepath, self.fieldnames, "shop_id")
        