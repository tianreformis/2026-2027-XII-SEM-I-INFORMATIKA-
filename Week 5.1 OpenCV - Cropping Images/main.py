import cv2 as cv

images = cv.imread("image.png")
print(images.shape)

y_start = 0
y_end = 600

x_start = 1
x_end = 600

cropping_image = images[x_start:x_end, y_start:y_end]

cv.imshow("Images ",cropping_image)
cv.waitKey(0)
cv.destroyAllWindows()