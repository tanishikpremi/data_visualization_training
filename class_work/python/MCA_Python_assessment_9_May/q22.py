# Q22. Read sales data from a CSV file using Pandas and plot a bar chart 
# representing product-wise sales using Matplotlib.

import pandas as pd
import matplotlib.pyplot as plt

def plot_sales():
    data = "Product,Sales\nA,150\nB,200\nC,100\nD,250"
    with open('product_sales.csv', 'w') as f: f.write(data)
    
    df = pd.read_csv('product_sales.csv')
    plt.bar(df['Product'], df['Sales'], color='skyblue')
    plt.title('Product-wise Sales')
    plt.xlabel('Product')
    plt.ylabel('Sales')
    
    plt.savefig('sales_bar_chart.png')
    print("Bar chart saved as 'sales_bar_chart.png'")

if __name__ == "__main__":
    plot_sales()

# Expected Output:
# Bar chart saved as 'sales_bar_chart.png'
