import cv2 as cv 

img = cv.imread("image.png")

# take properties from the image
tinggi, lebar, _ = img.shape
print (f"Info : Lebar {lebar}px, Tinggi {tinggi}px ")

#resize image
img = cv.resize(img, (int(lebar/2), int(tinggi/2)))

# draw rectangle to cover around image
cv.rectangle(img, (0, 0), (lebar, tinggi), (0, 0, 255), 20)

# draw text on the image
text ="Presiden Terbaik Versi Mulya Adi"
font = cv.FONT_ITALIC
tickness = 2
textColor= (255, 255, 255)
textFontSize = 1
cv.putText(img, text, (15, tinggi-15), font, textFontSize, textColor, tickness, cv.LINE_AA)

#save the image as the new file 
newFileName = "newImage.png"
cv.imwrite(newFileName, img)
print(f"Image saved as {newFileName}")

#show image
cv.imshow("Image", img)
cv.waitKey(0)