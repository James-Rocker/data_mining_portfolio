import matplotlib.pyplot as plt

# Load the image into an array: image
image = plt.imread('900px-Astronaut-EVA.jpg')

# Extract minimum and maximum values from the image: p_min, p_max
p_min, p_max = image.min(), image.max()
print("The smallest & largest pixel intensities are %d & %d." % (p_min, p_max))

# Rescale the pixels: rescaled_image
rescaled_image = 256 * (image - p_min) / (p_max - p_min)
print("The rescaled smallest & largest pixel intensities are %.1f & %.1f." %
      (rescaled_image.min(), rescaled_image.max()))

# Display the original image in the top subplot
plt.subplot(2, 1, 1)
plt.title('original image')
plt.axis('off')
plt.imshow(image)

# Display the rescaled image in the bottom subplot
plt.subplot(2, 1, 2)
plt.title('rescaled image')
plt.axis('off')
plt.imshow(rescaled_image)

plt.show()
