# Q31. Plot a pie chart showing market share of different smartphone brands 
# and highlight the brand with maximum market share.

import matplotlib.pyplot as plt

def plot_market_share():
    brands = ['Samsung', 'Apple', 'Xiaomi', 'Oppo', 'Vivo']
    shares = [22, 21, 14, 10, 9]
    
    # Highlight the brand with max share (Samsung)
    explode = (0.1, 0, 0, 0, 0)
    
    plt.pie(shares, explode=explode, labels=brands, autopct='%1.1f%%', shadow=True, startangle=140)
    plt.title('Smartphone Market Share')
    
    plt.savefig('market_share_pie.png')
    print("Pie chart saved as 'market_share_pie.png'")

if __name__ == "__main__":
    plot_market_share()

# Expected Output:
# Pie chart saved as 'market_share_pie.png'
