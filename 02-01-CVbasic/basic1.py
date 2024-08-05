# Accessing opencv module
import cv2
import imutils

# load the image 
image = cv2.imread("suram.jpg")

# chek image size 
height,width,depth = image.shape
print("image size: ", height, width, depth)

# show the image 
cv2.imshow("suram.jpg", image)
cv2.waitKey(0)

# resize the image to 200x200px, ignoring aspect ratio
resized = cv2.resize(image, (200, 400))
cv2.imshow("SAAD JA", resized)
cv2.waitKey(0)

# crop the image 
cropped_image = image[30:100, 30:100]
cv2.imshow("Ceopped image", cropped_image)
cv2.waitKey(0)

# rotation can also be easily accomplished via imutils with less code
rotated = imutils.rotate(image, 45)
cv2.imshow("SAAD JA", rotated)
cv2.waitKey(0) 

# apply a Gaussian blur with a 11x11 kernel to the image to smooth it,
# useful when reducing high frequency noise
blurred = cv2.GaussianBlur(image, (11, 11), 0)
cv2.imshow("Blurred", blurred)
cv2.waitKey(0)


 # Drawing & color

# draw a blue 20px (filled in) circle on the image centered at
# x=300,y=150
output = image.copy()
cv2.circle(output, (300, 150), 20, (255, 0, 0), -1)
cv2.imshow("Circle", output)
cv2.waitKey(0)

# draw a 2px thick red rectangle surrounding the face
output = image.copy()
cv2.rectangle(output, (10, 10), (100, 120), (255, 0, 0), 2)
cv2.imshow("Rectangle", output)
cv2.waitKey(0)

# draw a 5px thick red line from x=60,y=20 to x=400,y=200
output = image.copy()
cv2.line(output, (0, 0), (250, 250), (0, 0, 255), 5)
cv2.line(output, (250, 0), (0, 250), (0, 0, 255), 5)
cv2.imshow("Line", output)
cv2.waitKey(0)


# draw green text on the image
output = image.copy()
cv2.putText(output, "MOVE ON MY SELF", (100, 100), 
	cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
cv2.imshow("Text", output)
cv2.waitKey(0)

