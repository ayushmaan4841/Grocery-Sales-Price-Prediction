# Grocery Sales Price Prediction

This repository contains a machine learning model built using Linear Regression to predict grocery sales prices based on various features such as product type, store location, promotional discounts, seasonal effects, and more. The project is implemented in Python using the **Scikit-learn** library.

## Table of Contents

- [Installation](#installation)  
- [Dataset](#dataset)  
- [Features](#features)  
- [Model](#model)  
- [Usage](#usage)  
- [Evaluation](#evaluation)  
- [Contributing](#contributing)  
- [License](#license)  

## Installation  

Clone the repository to your local machine using:  

```bash
git clone https://github.com/ayushmaan4841/Grocery-Sales-Price-Prediction.git
```

Navigate to the project directory:  

```bash
cd Grocery-Sales-Price-Prediction
```

Install the required dependencies:  

```bash
pip install -r requirements.txt
```

If you don't have a `requirements.txt` file yet, you can create one with the necessary libraries:  

```txt
pandas
numpy
scikit-learn
```

## Dataset  

The dataset used for this project includes the following features:  

- **product_type**: Category of the grocery item (e.g., dairy, bakery, beverages).  
- **store_location**: Geographical location of the store.  
- **discount_applied**: Discount percentage on the product.  
- **season**: The season (e.g., winter, summer, fall).  
- **weekend**: Whether the sale happened on a weekend (1 for Yes, 0 for No).  
- **store_size**: The size of the store (small, medium, large).  
- **demand_index**: A score indicating the demand for a product.  
- **price**: The target variable representing the sales price of the grocery item.  

For demonstration, the dataset used is simulated, but you can replace it with a real-world dataset by loading it from a CSV file.  

## Features  

The model is trained on the following features:  

- **product_type**: Type of grocery item.  
- **store_location**: Geographical store location.  
- **discount_applied**: Discount percentage on the product.  
- **season**: The season of the sale.  
- **weekend**: Whether the sale happened on a weekend.  
- **store_size**: Size of the store.  
- **demand_index**: A numerical score reflecting product demand.  

## Model  

The machine learning model used in this project is **Linear Regression** from Scikit-learn. The model predicts grocery sales prices based on the features listed above.  

### Steps in the Model:  

1. **Data Preprocessing**: Handle missing values, feature scaling, and encode categorical data if necessary.  
2. **Model Training**: Train the model using the training dataset.  
3. **Prediction**: Predict grocery sales prices for the test dataset or for new input data.  
4. **Evaluation**: Evaluate the model's performance using metrics like Mean Squared Error and R² score.  

## Usage  

Ensure you have installed the required dependencies using:  

```bash
pip install -r requirements.txt
```

Run the Python script to train the model and predict grocery sales prices:  

```bash
python grocery_sales_prediction.py
```

To predict sales prices for new data, modify the `new_data` array in the script and rerun it. Example:  

```python
new_data = [[1, 2, 10, "Winter", 1, "Large", 8]]  # Sample input data
predicted_price = model.predict(new_data)
print("Predicted Price:", predicted_price)
```

## Evaluation  

The model’s performance is evaluated using the following metrics:  

- **Mean Squared Error (MSE)**: Measures the average squared difference between predicted and actual sales prices.  
- **R² Score**: Represents the proportion of variance in sales price that is predictable from the features. A higher score means a better model.  

Sample output might look like this:  

```txt
Mean Squared Error: 500000.0
R^2 Score: 0.92
Predicted Prices: [120.50, ...]
```

## Contributing  

Contributions are welcome! Feel free to submit a pull request or open an issue to suggest improvements or fixes. Here's how you can contribute:  

1. Fork the repository.  
2. Create a new branch (`git checkout -b feature-branch`).  
3. Make your changes.  
4. Push to your branch (`git push origin feature-branch`).  
5. Open a Pull Request.  

# License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
```

## How to Use:
- Copy the above content into a file named **`README.md`** in your GitHub repository.
- Replace the placeholder repository URL (`https://github.com/ayushmaan4841/Grocery-Sales-Price-Prediction.git`) with the actual URL of your project.
