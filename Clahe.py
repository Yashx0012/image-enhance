import cv2
import matplotlib.pyplot as plt

# Load image
image = cv2.imread('778.png')

lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)

l, a, b = cv2.split(lab)

# Apply CLAHE
clahe = cv2.createCLAHE(clipLimit=4.0, tileGridSize=(8,8))
l = clahe.apply(l)

lab = cv2.merge((l, a, b))

result = cv2.cvtColor(lab, cv2.COLOR_LAB2RGB)
plt.imshow(result)
plt.title("CLAHE")
plt.axis('off')
plt.show()