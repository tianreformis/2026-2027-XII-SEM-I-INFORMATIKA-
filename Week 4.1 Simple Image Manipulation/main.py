import cv2 as cv 

image = cv.imread('image.png')
black_and_white_filtered = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
gaussian_blur = cv.GaussianBlur(image, (5, 5), 0)

gaussian_black_and_white_filtered = cv.GaussianBlur(black_and_white_filtered, (5, 5), 0)

cv.imshow('Original', image)
cv.imshow('Filtered', gaussian_blur)
cv.imshow('Filtered (BW)', gaussian_black_and_white_filtered)

cv.waitKey(0)
cv.destroyAllWindows()