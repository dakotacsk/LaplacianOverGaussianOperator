from edge_detection import LoGEdgeDetector
from skimage import io
import matplotlib.pyplot as plt

# Load the image
img_path = "img/spherical_cow.jpeg" # If you choose a larger image with a lot of details, it might take a while to load. Example provided in koala image.
img = io.imread(img_path)
img = img.astype(float) / 255  # Normalize the image to [0, 1]

# Visualize the original image
plt.figure(figsize=(6, 6))
plt.imshow(img, cmap='gray')
plt.title('Original Image')
plt.axis('off')
plt.show()

# Apply first derivative (Sobel), second derivative (Laplacian), and simple Laplacian
fig, axs = plt.subplots(1, 2, figsize=(10, 5))

# First Derivative - Sobel
sobel_result = LoGEdgeDetector.first_derivative_sobel(img)
axs[0].imshow(sobel_result, cmap='gray')
axs[0].axis('off')
axs[0].set_title('First Derivative - Sobel')

# Second Derivative - Laplacian
laplacian_result = LoGEdgeDetector.second_derivative_laplacian(img)
zero_crossed_laplacian = LoGEdgeDetector.zero_crossing(laplacian_result)
axs[1].imshow(zero_crossed_laplacian, cmap='gray')
axs[1].axis('off')
axs[1].set_title('Second Derivative - Laplacian')

# Apply Gaussian Laplace function and visualize the results for different sigma values
sigma_values = [2, 4, 6, 8]
fig, axs = plt.subplots(1, 4, figsize=(20, 5))
for i, sigma in enumerate(sigma_values):
    result = LoGEdgeDetector.gaussian_laplace(img, sigma=sigma)
    zero_crossed = LoGEdgeDetector.zero_crossing(result)
    axs[i].imshow(zero_crossed, cmap='gray')
    axs[i].axis('off')
    axs[i].set_title(f'LoG with $\sigma={sigma}$')
plt.tight_layout()
plt.show()
