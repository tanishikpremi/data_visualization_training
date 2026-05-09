# Q14. Create a line chart using Matplotlib to display monthly sales data 
# of a company. Add title, labels, legend, and grid for better visualization.

import matplotlib.pyplot as plt

def plot_sales():
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
    sales = [15000, 18000, 16000, 22000, 25000]
    
    plt.plot(months, sales, marker='o', label='Sales')
    plt.title('Monthly Sales Data')
    plt.xlabel('Month')
    plt.ylabel('Sales ($)')
    plt.legend()
    plt.grid(True)
    
    plt.savefig('sales_line_chart.png')
    print("Line chart saved as 'sales_line_chart.png'")

if __name__ == "__main__":
    plot_sales()

# Expected Output:
# Line chart saved as 'sales_line_chart.png'
