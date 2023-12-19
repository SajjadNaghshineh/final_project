import os
os.system("cls")
import pandas as pd

products_header = ["product_id", "product_name", "company_name", "production_date", "expiration_period", "bought_count", "available_count", "price"]

customers_header = ["username", "fullname", "user_id", "phone", "total_buy", "paid_amount", "unpaid_amount", "credit", "discount"]

orders_header = ["order_id", "username", "shop_id", "product_id", "quantity", "order_date", "recieve_date"]

shops_header = ["shop_id", "shop_name", "unsend_orders", "total_sell"]

data = {
    "x": [1, 1, 3],
    "y": [4, 5, 6]
}

df = pd.DataFrame(data)
x = df[df["x"] == 1]["y"].values
print(x)
print(750000 // 500000)
