#Price Distribution
plt.figure(figsize=(10, 6))
sns.histplot(sales_data['price'], bins=50)
plt.title('Price Distribution')
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.show()

#Sales vs Price Scatter Plot
plt.figure(figsize=(10, 6))
sns.scatterplot(x='price', y='sales', data=sales_data)
plt.title('Sales vs Price')
plt.xlabel('Price')
plt.ylabel('Sales')
plt.show()

#Price Elasticity Histogram
data['price_elasticity'] = data['log_sales'] / data['log_price']
plt.figure(figsize=(10, 6))
sns.histplot(data['price_elasticity'], bins=50)
plt.title('Price Elasticity Distribution')
plt.xlabel('Price Elasticity')
plt.ylabel('Frequency')
plt.show()

#Residuals Plot
residuals = y_test - predictions
plt.figure(figsize=(10, 6))
sns.histplot(residuals, bins=50)
plt.title('Residuals Distribution')
plt.xlabel('Residuals')
plt.ylabel('Frequency')
plt.show()

#Feature Importance Plot
importances = model.feature_importances_
features = X.columns
indices = np.argsort(importances)
plt.figure(figsize=(10, 6))
plt.title('Feature Importances')
plt.barh(range(len(indices)), importances[indices], align='center')
plt.yticks(range(len(indices)), [features[i] for i in indices])
plt.xlabel('Relative Importance')
plt.show()

#Monthly Sales Trends:
sales_data['date'] = pd.to_datetime(sales_data['date'])
sales_data['month'] = sales_data['date'].dt.to_period('M')
monthly_sales = sales_data.groupby('month')['sales'].sum().reset_index()
plt.figure(figsize=(12, 6))
plt.plot(monthly_sales['month'].astype(str), monthly_sales['sales'])
plt.title('Monthly Sales Trends')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.xticks(rotation=45)
plt.show()

#Sales Distribution by Product Category:
category_sales = data.groupby('category')['sales'].sum().reset_index()

plt.figure(figsize=(12, 6))
sns.barplot(x='category', y='sales', data=category_sales)
plt.title('Sales Distribution by Product Category')
plt.xlabel('Category')
plt.ylabel('Sales')
plt.xticks(rotation=45)
plt.show()
