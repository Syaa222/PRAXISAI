from PIL import Image
import face_recognition
import cv2

# Load the jpg file into a numpy array
image = face_recognition.load_image_file("bowon.jpg")
print(image.shape, image.dtype)
# Find all the faces in the image using the default HOG-based model.
# This method is fairly accurate, but not as accurate as the CNN model and not GPU accelerated.
# See also: find_faces_in_picture_cnn.py
face_locations = face_recognition.face_locations(image)

print("I found {} face(s) in this photograph.".format(len(face_locations)))

for face_location in face_locations:

    # Print the location of each face in this image
    top, right, bottom, left = face_location
    print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))

    # You can access the actual face itself like this:
    face_image = image[top:bottom, left:right]
    pil_image = Image.fromarray(face_image)
    pil_image.show()

# draw a 2px thick red rectangle surrounding the face
output = image.copy()
cv2.rectangle(output, (10, 10), (100, 120), (255, 0, 0), 2)
cv2.imshow("Rectangle", output)
cv2.waitKey(0)