import cv2

cap =cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
color=(255,0,255)
cap.set(10,100)

faceCascade = cv2.CascadeClassifier("assets/haarcascade_frontalface_default.xml")
noplateCascade = cv2.CascadeClassifier("assets/haarcascade_russian_plate_number.xml")



while True:
    success, img =cap.read()
    # img = cv2.imread("assets/rahul.webp")

    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)



    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        numberplate = noplateCascade.detectMultiScale(imgGray, 1.1, 4)
        for (a, b, c, d) in numberplate:
            area = c * d
            if area > 500:
                cv2.rectangle(img, (a, b), (a +c, b + d), (255, 0, 255), 2)
                cv2.putText(img, "number plate", (a, b - 5), cv2.FONT_HERSHEY_COMPLEX, 1, color, 1)

                imageroi = img[b:b + d, a:a + c]
                cv2.imshow("roi", imageroi)

        cv2.imshow("image", img)

        # cv2.imshow("video",img)

        # if cv2.waitKey(1) & 0xFF == ord('s'):
        #     cv2.imwrite("assets/saved/NoPlate_" + str(count) + ".jpg", imageroi)
        #     cv2.rectangle(img, (0, 200), (640, 300), (0, 255, 0), cv2.FILLED)
        #     cv2.putText(img, "Scan Saved", (150, 265), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 0, 225), 2)
        #     cv2.imshow("Result", img)
        #     count = count + 1
        #     cv2.waitKey(500)
    # cv2.imshow("image", img)


    cv2.imshow("video",img)

    # if True:
    #     while True:
    #
    #
    #
    #         numberplate = noplateCascade.detectMultiScale(imgGray, 1.1, 4)
    #         for (a, b, w, h) in numberplate:
    #             area = w * h
    #             if area > 500:
    #                 cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 2)
    #                 cv2.putText(img, "number plate", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 1, color, 1)
    #
    #                 imageroi = img[y:y + h, x:x + w]
    #                 cv2.imshow("roi", imageroi)
    #
    #         cv2.imshow("image", img)
    #
    #         # cv2.imshow("video",img)
    #
    #         if cv2.waitKey(1) & 0xFF == ord('s'):
    #             cv2.imwrite("assets/saved/NoPlate_" + str(count) + ".jpg", imageroi)
    #             cv2.rectangle(img, (0, 200), (640, 300), (0, 255, 0), cv2.FILLED)
    #             cv2.putText(img, "Scan Saved", (150, 265), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 0, 225), 2)
    #             cv2.imshow("Result", img)
    #             count = count + 1
    #             cv2.waitKey(500)

    if cv2.waitKey(1)&0xFF==ord('q'):
        break