import cv2

img=cv2.imread("solar-system.jpg")
cv2.putText(img,
            "SUN",
            (20,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )
cv2.putText(img,
            "Mercury",
            (120,240),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )
cv2.putText(img,
            "Venus",
            (200,260),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )
cv2.putText(img,
            "Earth",
            (290,270),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )
cv2.putText(img,
            "Mars",
            (380,260),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )

cv2.putText(img, 
            "Jupiter",
            (400,320), 
            fontFace= cv2.FONT_HERSHEY_COMPLEX,
            fontScale= 0.5, color=(255,255,255))

cv2.putText(img,
            "Saturn", 
            (460,340), 
            fontFace= cv2.FONT_HERSHEY_COMPLEX, 
            fontScale= 0.5, 
            color=(255,255,255))

cv2.putText(img, 
            "Uranus", 
            (560,370), 
            fontFace= cv2.FONT_HERSHEY_COMPLEX, 
            fontScale= 0.5, 
            color=(255,255,255))

cv2.putText(img, 
            "Neptune", 
            (1112,287), 
            fontFace= cv2.FONT_HERSHEY_COMPLEX, 
            fontScale= 0.5, 
            color=(255,255,255))

cv2.imshow("output",img)
cv2.waitKey(3000)



