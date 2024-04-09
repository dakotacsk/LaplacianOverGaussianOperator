from edge_detection import LoGEdgeDetector
from skimage import io
import matplotlib.pyplot as plt

# Load the image
img_path = "img/spherical_cow.jpeg"
img = io.imread(img_path)
plt.imshow(img)
img = img.astype(float) / 255  # Normalize the image to [0, 1]

# Apply Gaussian Laplace function and visualize the results for different sigma values
sigma_values = [1, 2, 3, 4]
fig, axs = plt.subplots(1, 4, figsize=(20, 5))

for i, sigma in enumerate(sigma_values):
    result = LoGEdgeDetector.gaussian_laplace(img, sigma=sigma)
    zero_crossed = LoGEdgeDetector.zero_crossing(result)
    axs[i].imshow(zero_crossed, cmap='gray')
    axs[i].axis('off')
    axs[i].set_title(f'LoG with $\sigma={sigma}$')

plt.tight_layout()
plt.show()
