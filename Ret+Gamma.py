import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load image
image = cv2.imread('778.png')

# Retinex
def retinex(img, sigma_list=[15, 80, 250]):
    img = img.astype(np.float32) / 255.0
    retinex = np.zeros_like(img)

    for sigma in sigma_list:
        blur = cv2.GaussianBlur(img, (0, 0), sigma)
        retinex += np.log10(img + 1e-6) - np.log10(blur + 1e-6)

    retinex = retinex / len(sigma_list)
    retinex = np.exp(retinex)

    # Normalize
    retinex = (retinex - retinex.min()) / (retinex.max() - retinex.min())
    retinex = (retinex * 255).astype(np.uint8)

    return retinex

retinex_img = retinex(image)

# Gamma Correction
gamma = 1.5   # adjust (1.2 to 2.0)

inv_gamma = 1.0 / gamma
table = np.array([((i / 255.0) ** inv_gamma) * 255
                  for i in range(256)]).astype("uint8")

final = cv2.LUT(retinex_img, table)

# Convert to RGB for display
final_rgb = cv2.cvtColor(final, cv2.COLOR_BGR2RGB)

# Show result
plt.imshow(final_rgb)
plt.title("Retinex + Gamma")
plt.axis('off')
plt.show()