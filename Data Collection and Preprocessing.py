import pandas as pd
import numpy as np

product_data = pd.read_csv('product_data.csv')
sales_data = pd.read_csv('sales_data.csv')
customer_data = pd.read_csv('customer_data.csv')

sales_data.dropna(inplace=True)
sales_data = sales_data[sales_data['price'] > 0]

sales_data['log_price'] = np.log(sales_data['price'])
sales_data['log_sales'] = np.log(sales_data['sales'])

data = sales_data.merge(product_data, on='product_id').merge(customer_data, on='customer_id')
