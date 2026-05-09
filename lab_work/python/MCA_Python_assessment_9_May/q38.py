# Q38. Generate random temperature data using NumPy and plot a 
# histogram representing temperature distribution.

import numpy as np
import matplotlib.pyplot as plt

def plot_temp_histogram():
    np.random.seed(42)
    # Generate 365 days of temperatures with mean 25C and std 5C
    temps = np.random.normal(25, 5, 365)
    
    plt.hist(temps, bins=20, color='coral', edgecolor='black')
    plt.title('Annual Temperature Distribution')
    plt.xlabel('Temperature (°C)')
    plt.ylabel('Frequency (Days)')
    
    plt.savefig('temp_histogram.png')
    print("Histogram saved as 'temp_histogram.png'")

if __name__ == "__main__":
    plot_temp_histogram()

# Expected Output:
# Histogram saved as 'temp_histogram.png'
