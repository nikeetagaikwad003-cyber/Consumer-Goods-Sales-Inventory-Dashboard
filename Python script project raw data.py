import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Set random seed for reproducibility
np.random.seed(42)

# Generate DimDate
start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 12, 31)
date_range = pd.date_range(start_date, end_date, freq='D')
dim_date = pd.DataFrame({'Date': date_range})
dim_date['Month'] = dim_date['Date'].dt.month
dim_date['Quarter'] = dim_date['Date'].dt.quarter
dim_date['Year'] = dim_date['Date'].dt.year
dim_date['IsHoliday'] = np.where(dim_date['Date'].dt.weekday >= 5, 1, 0)
dim_date['WeekdayName'] = dim_date['Date'].dt.day_name()

# Generate DimProduct
product_ids = range(1001, 1021)
categories = ['Beverages', 'Snacks', 'Dairy', 'Household']
brands = ['BrandA', 'BrandB', 'BrandC', 'BrandD']
dim_product = pd.DataFrame({
    'ProductID': product_ids,
    'ProductName': [f'Product_{i}' for i in product_ids],
    'Category': np.random.choice(categories, len(product_ids)),
    'Brand': np.random.choice(brands, len(product_ids)),
    'UnitSize': np.random.choice(['250ml', '500ml', '1L', '5kg', '1kg'], len(product_ids)),
    'IsDiscontinued': np.random.choice([0, 1], len(product_ids), p=[0.9, 0.1])
})

# Generate DimCustomer
customer_ids = range(201, 251)
segments = ['Retail', 'Wholesale']
regions = ['North', 'South', 'East', 'West']
loyalty_levels = ['Silver', 'Gold', 'Platinum']
dim_customer = pd.DataFrame({
    'CustomerID': customer_ids,
    'Name': [f'Customer_{i}' for i in customer_ids],
    'Segment': np.random.choice(segments, len(customer_ids)),
    'Region': np.random.choice(regions, len(customer_ids)),
    'LoyaltyLevel': np.random.choice(loyalty_levels, len(customer_ids))
})

# Generate DimStore
store_ids = range(301, 311)
store_types = ['Retail', 'Online']
dim_store = pd.DataFrame({
    'StoreID': store_ids,
    'StoreName': [f'Store_{i}' for i in store_ids],
    'Region': np.random.choice(regions, len(store_ids)),
    'StoreType': np.random.choice(store_types, len(store_ids))
})

# Generate FactSales
num_sales = 5000
fact_sales = pd.DataFrame({
    'SaleID': range(1, num_sales + 1),
    'Date': np.random.choice(date_range, num_sales),
    'ProductID': np.random.choice(product_ids, num_sales),
    'CustomerID': np.random.choice(customer_ids, num_sales),
    'StoreID': np.random.choice(store_ids, num_sales),
    'QuantitySold': np.random.randint(1, 10, num_sales),
    'UnitPrice': np.random.uniform(10, 100, num_sales).round(2),
    'Discount': np.random.choice([0, 0.05, 0.1, 0.15], num_sales),
    'Cost': np.random.uniform(5, 80, num_sales).round(2)
})

# Generate FactInventory
inventory_records = 1500
fact_inventory = pd.DataFrame({
    'InventoryID': range(1, inventory_records + 1),
    'ProductID': np.random.choice(product_ids, inventory_records),
    'StoreID': np.random.choice(store_ids, inventory_records),
    'Date': np.random.choice(date_range, inventory_records),
    'OpeningStock': np.random.randint(10, 100, inventory_records),
    'ReceivedStock': np.random.randint(0, 50, inventory_records),
    'SoldStock': np.random.randint(0, 50, inventory_records)
})
fact_inventory['ClosingStock'] = fact_inventory['OpeningStock'] + fact_inventory['ReceivedStock'] - fact_inventory['SoldStock']

# Optionally: Save to CSV
dim_date.to_csv('DimDate.csv', index=False)
dim_product.to_csv('DimProduct.csv', index=False)
dim_customer.to_csv('DimCustomer.csv', index=False)
dim_store.to_csv('DimStore.csv', index=False)
fact_sales.to_csv('FactSales.csv', index=False)
fact_inventory.to_csv('FactInventory.csv', index=False)


