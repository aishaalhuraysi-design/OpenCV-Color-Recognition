import cv2
import numpy as np

image = cv2.imread("3pools.jpg")
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# حدود الألوان
colors = {
    "Red": (
        np.array([0, 120, 70]),
        np.array([10, 255, 255])
    ),
    "Green": (
        np.array([35, 50, 50]),
        np.array([85, 255, 255])
    ),
    "Blue": (
        np.array([100, 150, 50]),
        np.array([140, 255, 255])
    )
}

for color_name, (lower, upper) in colors.items():

    mask = cv2.inRange(hsv, lower, upper)

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:

        area = cv2.contourArea(cnt)

        if area > 500:

            x, y, w, h = cv2.boundingRect(cnt)

            cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

            cv2.putText(image,
                        color_name,
                        (x, y-10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.8,
                        (0, 255, 0),
                        2)

cv2.imshow("Color Recognition", image)

cv2.waitKey(0)
cv2.destroyAllWindows()