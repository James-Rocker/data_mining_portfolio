import matplotlib.pyplot as plt

# TODO: put all of these functions within a custom function

# Load the image into an array: img
img = plt.imread('900px-Astronaut-EVA.jpg')

# Print the shape of the image
print(img.shape)

# Compute the sum of the red, green and blue channels: intensity
intensity = img.sum(axis=2)

# Print the shape of the intensity
print(intensity.shape)

# Display the intensity with a colormap of 'gray'
plt.imshow(intensity, cmap='gray')

# Add a color bar
plt.colorbar()

# Hide the axes and show the figure
plt.axis('off')
plt.show()
