import cv2

img = cv2.imread("solar-system.jpg")

cv2.imshow("Display Image",img)

print(img)

cv2.waitkey(0)

cv2.putText(img,
            "Sun",
            (20,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )

cv2.putText(img,
            "Mercury",
            (40,320),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (355,355,355)
            )

cv2.putText(img,
            "Venus",
            (60,340),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (455,455,455)
            )

cv2.putText(img,
            "Earth",
            (80,360),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (555,555,555)
            )

cv2.putText(img,
            "Mars",
            (100,380),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (655,655,655)
            )

cv2.putText(img,
            "Jupiter",
            (120,400),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (755,755,755)
            )

cv2.putText(img,
            "Saturn",
            (140,420),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (855,855,855)
            )

cv2.putText(img,
            "Uranus",
            (160,440),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (955,955,955)
            )

cv2.putText(img,
            "Sun",
            (180,460),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (1005,1005,1005)
            )

img = cv2.imwrite("Solar_systemwithname.jpg",img)