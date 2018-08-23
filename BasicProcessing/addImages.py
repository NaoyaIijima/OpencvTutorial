import cv2

img1 = cv2.imread("images/face.jpeg")
img2 = cv2.imread("images/road.jpeg")

for i in range(0,10,1):
    res = cv2.addWeighted(img1, 1-i*0.1, img2, i*0.1, 0)
    cv2.imshow("image", res)
    key = cv2.waitKey(0)
    if key == ord("q"):
        break

cv2.destroyAllWindows()
