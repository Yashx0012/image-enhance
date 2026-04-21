import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load image
image = cv2.imread('778.png')

# CLAHE
lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
l, a, b = cv2.split(lab)

clahe = cv2.createCLAHE(clipLimit=4.0, tileGridSize=(8,8))
l = clahe.apply(l)

lab = cv2.merge((l, a, b))
clahe_img = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)

# Gamma Correction
gamma = 1.5   # try 1.2 to 2.0
inv_gamma = 1.0 / gamma
table = np.array([((i/255.0)**inv_gamma)*255 for i in range(256)]).astype("uint8")

final = cv2.LUT(clahe_img, table)

final_rgb = cv2.cvtColor(final, cv2.COLOR_BGR2RGB)

plt.imshow(final_rgb)
plt.title("CLAHE + Gamma")
plt.axis('off')
plt.show()