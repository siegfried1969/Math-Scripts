import numpy as np
import matplotlib.pyplot as plt

# Generate x values from -10 to 10
x = np.linspace(-10, 10, 400)

# Calculate corresponding y values for the parabola y = x^2
y = x**2

# Create the plot
plt.figure(figsize=(8, 6))
plt.plot(x, y, label='y = x^2', color='blue', linewidth=2)

# Add titles and labels
plt.title('Simple Parabola Plot')
plt.xlabel('x')
plt.ylabel('y')

# Add origin axes and grid lines for clarity
plt.axhline(0, color='black', linewidth=1, alpha=0.5)
plt.axvline(0, color='black', linewidth=1, alpha=0.5)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()

# Display the plot window
plt.show()