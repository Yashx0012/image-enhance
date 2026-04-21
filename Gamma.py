import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load image
image = cv2.imread('778.png')

# Gamma value 
gamma = 1.5  

inv_gamma = 1.0 / gamma

# Create lookup table
table = np.array([((i / 255.0) ** inv_gamma) * 255
                  for i in range(256)]).astype("uint8")

# Apply gamma correction
result = cv2.LUT(image, table)


result_rgb = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)

plt.imshow(result_rgb)
plt.title("Gamma")
plt.axis('off')
plt.show()