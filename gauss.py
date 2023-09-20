import numpy as np
import matplotlib.pyplot as plt

# Define the Gaussian function
def gaussian(x, mu, sigma):
    return np.exp(-((x - mu) ** 2) / (2 * sigma ** 2))

# Create an array of x values
x = np.linspace(0, np.pi, 500)  # Adjust the number of points as needed for smoothness

# Define the parameters of the Gaussian function with increased sigma
mu = np.pi / 2  # Center of the Gaussian
sigma = 0.5    # Increased width of the Gaussian

# Calculate the Gaussian curve
y = gaussian(x, mu, sigma)

# Create a figure and plot the Gaussian curve
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='Gaussian Curve')

# Add labels and legend
plt.xlabel('x')
plt.ylabel('Amplitude')
plt.legend(loc='upper right')
plt.title('Gaussian Distribution Curve with Increased Width')

# Show the plot
plt.grid(True)
plt.show()
