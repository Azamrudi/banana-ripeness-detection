import cv2
import numpy as np

img = cv2.imread('images/sample_input.jpg')
img = cv2.resize(img, (300, 300))

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_green = np.array([35, 50, 50])
upper_green = np.array([85, 255, 255])

lower_yellow = np.array([20, 100, 100])
upper_yellow = np.array([35, 255, 255])

mask_green = cv2.inRange(hsv, lower_green, upper_green)
mask_yellow = cv2.inRange(hsv, lower_yellow, upper_yellow)

green_pixels = np.sum(mask_green > 0)
yellow_pixels = np.sum(mask_yellow > 0)

if green_pixels > yellow_pixels:
    print("Mentah")
else:
    print("Matang")