import cv2


def captch_ex(file_name):
    img = cv2.imread(file_name)

    img_final = cv2.imread(file_name)
    img2gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(img2gray, 180, 255, cv2.THRESH_BINARY)
    image_final = cv2.bitwise_and(img2gray, img2gray, mask=mask)
    ret, new_img = cv2.threshold(image_final, 180, 255, cv2.THRESH_BINARY)
    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
    dilated = cv2.dilate(new_img, kernel, iterations=9)
    contours, hierarchy = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    for contour in contours:
        # get rectangle bounding contour
        [x, y, w, h] = cv2.boundingRect(contour)

        # Don't plot small false positives that aren't text
        if w < 35 and h < 35:
            continue

        # draw rectangle around contour on original image
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 2)

    cv2.namedWindow(file_name)
    cv2.imshow(file_name, img)
    while True:
        k = cv2.waitKey(100)
        if k == 27:
            print('ESC Exit')
            break
        elif k > -1:
            print('Other key Exit')
            break

        if cv2.getWindowProperty(file_name, cv2.WND_PROP_VISIBLE) < 1:
            print('Close window Exit')
            break
    cv2.destroyAllWindows()


file_name = 'your_image.jpg'
captch_ex(file_name)
file_name = 'img.png'
captch_ex(file_name)
