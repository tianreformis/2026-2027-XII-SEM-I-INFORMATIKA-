import cv2 as cv


img = cv.imread("Foto.jpg")

print(img.shape)
y_start = 175
y_end = 750

x_start = 0
x_end = 700

cropping_img = img[x_start:x_end, y_start:y_end]

tinggi,lebar,_= cropping_img.shape

 #cv.rectangle(cropping_img, (0,450) 
             #, (lebar, tinggi), (0,150, 255),1)

cv.line(cropping_img, (235,430),(325,430),(0,150,255),thickness=1)

text ="''Janganlah kamu berbuat seolah-"
font = cv.FONT_HERSHEY_PLAIN
tickness = 1
textColor = (255,255,255)
textFontSize = 1.5
cv.putText(cropping_img,text,(105, tinggi-500), font, textFontSize,
           textColor,tickness,cv.LINE_AA)

text ="olah kamu mau memerintah atas"
font = cv.FONT_HERSHEY_PLAIN
tickness = 1
textColor = (255,255,255)
textFontSize = 1.5
cv.putText(cropping_img,text,(105, tinggi-460), font, textFontSize,
           textColor,tickness,cv.LINE_AA)

text ="mereka yang dipercayakan"
font = cv.FONT_HERSHEY_PLAIN
tickness = 1
textColor = (255,255,255)
textFontSize = 1.5
cv.putText(cropping_img,text,(135, tinggi-420), font, textFontSize,
           textColor,tickness,cv.LINE_AA)

text ="kepadamu, tetapi hendaklah"
font = cv.FONT_HERSHEY_PLAIN
tickness = 1
textColor = (255,255,255)
textFontSize = 1.5
cv.putText(cropping_img,text,(100, tinggi-380), font, textFontSize,
           textColor,tickness,cv.LINE_AA)

text ="kamu"
font = cv.FONT_HERSHEY_PLAIN
tickness = 1
textColor = (0,200,255)
textFontSize = 1.5
cv.putText(cropping_img,text,(415, tinggi-380), font, textFontSize,
           textColor,tickness,cv.LINE_AA)

text ="menjadi"
font = cv.FONT_HERSHEY_PLAIN
tickness = 1
textColor = (0,200,255)
textFontSize = 1.5
cv.putText(cropping_img,text,(130, tinggi-340), font, textFontSize,
           textColor,tickness,cv.LINE_AA)

text ="TELADAN"
font = cv.FONT_HERSHEY_PLAIN
tickness = 1
textColor = (0,200,255)
textFontSize = 2
cv.putText(cropping_img,text,(230, tinggi-340), font, textFontSize,
           textColor,tickness,cv.LINE_AA)

text ="bagi"
font = cv.FONT_HERSHEY_PLAIN
tickness = 1
textColor = (255,255,255)
textFontSize = 1.5
cv.putText(cropping_img,text,(385, tinggi-340), font, textFontSize,
           textColor,tickness,cv.LINE_AA)

text ="kawanan domba itu.''"
font = cv.FONT_HERSHEY_PLAIN
tickness = 1
textColor = (255,255,255)
textFontSize = 1.5
cv.putText(cropping_img,text,(170, tinggi-300), font, textFontSize,
           textColor,tickness,cv.LINE_AA)

text ="1 Petrus 5:3"
font = cv.FONT_HERSHEY_PLAIN
tickness = 1
textColor = (255,255,255)
textFontSize = 1.5
cv.putText(cropping_img,text,(215, tinggi-220), font, textFontSize,
           textColor,tickness,cv.LINE_AA)

text ="@ayatalkitabharian"
font = cv.FONT_HERSHEY_PLAIN
tickness = 1
textColor = (255,255,255)
textFontSize = 0.9
cv.putText(cropping_img,text,(215, tinggi-50), font, textFontSize,
           textColor,tickness,cv.LINE_AA)

cv.imshow("img",cropping_img)
cv.waitKey(0)
cv.destoryALLWindows()