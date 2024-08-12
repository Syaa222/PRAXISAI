'''
COBA 02-01
'''
# Accessing opencv module
import cv2
import imutils

# load the image 
image = cv2.imread("Object.jpg")

# chek image size 
height,width,depth = image.shape
print("image size: ", height, width, depth)

# show the image 
cv2.imshow("Object.jpg", image)
cv2.waitKey(0)

# resize the image to 200x200px, ignoring aspect ratio
resized = cv2.resize(image, (200, 400))
cv2.imshow("Object.jpg", resized)
cv2.waitKey(0)

# crop the image 
cropped_image = image[30:100, 30:100]
cv2.imshow("Object.jpg", cropped_image)
cv2.waitKey(0)

# rotation can also be easily accomplished via imutils with less code
rotated = imutils.rotate(image, 45)
cv2.imshow("Object.jpg", rotated)
cv2.waitKey(0) 

# apply a Gaussian blur with a 11x11 kernel to the image to smooth it,
# useful when reducing high frequency noise
blurred = cv2.GaussianBlur(image, (11, 11), 0)
cv2.imshow("Object.jpg", blurred)
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


'''
COBA 02-02
'''
# import the necessary packages
import argparse
import cv2 
import imutils
'''
Detaction grey
'''
# load the input image (whose path was supplied via command line
# argument) and display the image to our screen
image = cv2.imread("Object.jpg")
cv2.imshow("Object.jpg", image)
cv2.waitKey(0)
# convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray", gray)
cv2.waitKey(0)

'''
Edge detec
'''
# applying edge detection we can find the outlines of objects in
# images
edged = cv2.Canny(gray, 30, 150)
cv2.imshow("Object.jpg", edged)
cv2.waitKey(0)

'''
Tressholding
'''
# threshold the image by setting all pixel values less than 225
# to 255 (white; foreground) and all pixel values >= 225 to 255
# (black; background), thereby segmenting the image
thresh = cv2.threshold(gray, 225, 255, cv2.THRESH_BINARY_INV)[1]
cv2.imshow("Object.jpg", thresh)
cv2.waitKey(0)

'''
Detecing object 
'''
# find contours (i.e., outlines) of the foreground objects in the
# thresholded image
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
output = image.copy()
# loop over the contours
for c in cnts:
	# draw each contour on the output image with a 3px thick purple
	# outline, then display the output contours one at a time
	cv2.drawContours(output, [c], -1, (240, 0, 159), 3)
	cv2.imshow("Object.jpg", output)
	cv2.waitKey(0)
	
'''
reslut object
'''
# draw the total number of contours found in purple
text = "I found {} objects!".format(len(cnts))
cv2.putText(output, text, (10, 25),  cv2.FONT_HERSHEY_SIMPLEX, 0.7,
	(240, 0, 159), 2)
cv2.imshow("Object.jpg", output)
cv2.waitKey(0)

'''
Erosien & Dilatation
'''
# we apply erosions to reduce the size of foreground objects
mask = thresh.copy()
mask = cv2.erode(mask, None, iterations=5)
cv2.imshow("Object.jpg", mask)
cv2.waitKey(0)

# similarly, dilations can increase the size of the ground objects
mask = thresh.copy()
mask = cv2.dilate(mask, None, iterations=5)
cv2.imshow("Object.jpg", mask)
cv2.waitKey(0)

'''
Masking and 
'''
# a typical operation we may want to apply is to take our mask and
# apply a bitwise AND to our input image, keeping only the masked
# regions
mask = thresh.copy()
output = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("Object.jpg", output)
cv2.waitKey(0) 