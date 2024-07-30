import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(10, 6))
sns.histplot(sales_data['price'], bins=50)
plt.title('Price Distribution')
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.show()

plt.figure(figsize=(10, 6))
sns.scatterplot(x='price', y='sales', data=sales_data)
plt.title('Sales vs Price')
plt.xlabel('Price')
plt.ylabel('Sales')
plt.show()
