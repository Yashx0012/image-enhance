import cv2
import matplotlib.pyplot as plt

# Load color image
image = cv2.imread('778.png')

# Convert BGR → YCrCb
ycrcb = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)

# Apply Histogram Equalization on Y channel
ycrcb[:, :, 0] = cv2.equalizeHist(ycrcb[:, :, 0])

# Convert back to RGB for display
result = cv2.cvtColor(ycrcb, cv2.COLOR_YCrCb2RGB)

# Show result
plt.imshow(result)
plt.title("Histogram Equalization (Color)")
plt.axis('off')
plt.show()