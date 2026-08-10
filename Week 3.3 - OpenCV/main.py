#alias supaya mempermudah pemanggilan library OpenCV
import cv2 as cv 

#Library open CV seperti perpustakaan, module buku buku, 

#var gambar
image = cv.imread("image.png") 
#imread, mengubah gambar jadi array matematis

cv.imshow("Tampil Gambar",image) 
#cv alias dari lib, imshow module, image parameter, properties

cv.waitKey(0)
cv.destroyAllWindows()