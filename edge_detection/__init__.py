from skimage import io
import numpy as np
from scipy.signal import convolve2d
from skimage.color import rgb2gray

class LoGEdgeDetector:
    @staticmethod
    def any_neighbor_zero(img, i, j):
        """Check if any neighbor of a pixel is zero."""
        for k in range(-1, 2):
            for l in range(-1, 2):
                if img[i+k, j+l] == 0:
                    return True
        return False

    @staticmethod
    def zero_crossing(img):
        """Detect zero crossings in an image and highlight them."""
        img[img > 0] = 1
        img[img < 0] = 0
        out_img = np.zeros(img.shape)
        for i in range(1, img.shape[0]-1):
            for j in range(1, img.shape[1]-1):
                if img[i, j] > 0 and LoGEdgeDetector.any_neighbor_zero(img, i, j):
                    out_img[i, j] = 255
        return out_img

    @staticmethod
    def gaussian_kernel(size, sigma=1.0):
        """Generates a 2D Gaussian kernel."""
        size = int(size) // 2
        x, y = np.mgrid[-size:size+1, -size:size+1]
        normal = 1 / (2.0 * np.pi * sigma**2)
        g = np.exp(-((x**2 + y**2) / (2.0*sigma**2))) * normal
        return g

    @staticmethod
    def laplacian_of_gaussian_kernel(size, sigma=1.0):
        """Generates a Laplacian of Gaussian (LoG) kernel."""
        size = int(size) // 2
        x, y = np.mgrid[-size:size+1, -size:size+1]
        normal = 1 / (np.pi * sigma**4)
        lo_g = ((x**2 + y**2 - (2.0 * sigma**2)) / (sigma**4)) * np.exp(-((x**2 + y**2) / (2.0*sigma**2))) * normal
        return lo_g

    @staticmethod
    def gaussian_laplace(img, sigma=1.0):
        """Applies the Laplacian of Gaussian (LoG) operator to an image."""
        if img.ndim > 2:
            img = rgb2gray(img)
        size = int(6*sigma + 1)
        lo_g_kernel = LoGEdgeDetector.laplacian_of_gaussian_kernel(size, sigma)
        img_filtered = convolve2d(img, lo_g_kernel, mode='same', boundary='fill', fillvalue=0)
        return img_filtered

    @staticmethod
    def first_derivative_sobel(img):
        """Applies a Sobel filter to compute the first derivative."""
        if img.ndim > 2:
            img = rgb2gray(img)
        sobel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
        sobel_y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
        img_x = convolve2d(img, sobel_x, mode='same', boundary='fill', fillvalue=0)
        img_y = convolve2d(img, sobel_y, mode='same', boundary='fill', fillvalue=0)
        return np.hypot(img_x, img_y)

    @staticmethod
    def second_derivative_laplacian(img):
        """Applies a Laplacian filter to compute the second derivative."""
        if img.ndim > 2:
            img = rgb2gray(img)
        laplacian_kernel = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])
        return convolve2d(img, laplacian_kernel, mode='same', boundary='fill', fillvalue=0)
