"""Colour detection using Open-CV"""
import os
import cv2
import numpy

image_path = input("Enter the name of the image file to read: ")
while not os.path.isfile(f"./{image_path}") or image_path.split(".")[1] not in ["jpg", "jpeg"]:
    image_path = input("Please enter the name of a JPEG file in the current directory: ")

image = cv2.imread(image_path)
COLOURS = [
    ([0, 0, 100], [70, 70, 255]),  # RED
    ([0, 100, 0], [80, 255, 80]),  # GREEN
    ([0, 180, 180], [50, 255, 255]),  # YELLOW
]

for lower, upper in COLOURS:
    lower = numpy.array(lower, dtype="uint8")
    upper = numpy.array(upper, dtype="uint8")

    mask = cv2.inRange(image, lower, upper)
    output = cv2.bitwise_and(image, image, mask=mask)

    cv2.imshow(image_path, numpy.hstack([image, output]))
    cv2.waitKey(0)

cv2.destroyAllWindows()
