import cv2
filepath ="ging.jpg"
image = cv2.imread(filepath,1)
cv2.imshow("ging",image)
cv2.waitKey(0)
cv2.destroyAllWindows()