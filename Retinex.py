import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load image
image = cv2.imread('778.png')

img = image.astype(np.float32) / 255.0

# Retinex function
def retinex(img, sigma_list=[15, 80, 250]):
    retinex = np.zeros_like(img)

    for sigma in sigma_list:
        blur = cv2.GaussianBlur(img, (0, 0), sigma)
        retinex += np.log10(img + 1e-6) - np.log10(blur + 1e-6)

    retinex = retinex / len(sigma_list)
    retinex = np.exp(retinex)

    retinex = (retinex - retinex.min()) / (retinex.max() - retinex.min())

    return (retinex * 255).astype(np.uint8)

# Apply Retinex
result = retinex(img)

result_rgb = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)

plt.imshow(result_rgb)
plt.title("Retinex")
plt.axis('off')
plt.show()