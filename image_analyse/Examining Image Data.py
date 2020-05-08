import matplotlib.pyplot as plt

# Load the image into an array: img
img = plt.imread('900px-Astronaut-EVA.jpg')

# Print the shape of the image
print(img.shape)

# Display the image pixel columns, rows then colour channels
plt.imshow(img)

# Hide the axes
plt.axis('off')
plt.show()
