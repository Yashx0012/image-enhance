import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('778.png')
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

plt.imshow(image_rgb)
plt.title("Original Color")
plt.axis('off')
plt.show()