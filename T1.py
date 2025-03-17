import cv2

# Вариант №8

def image_centering(image):
    img = cv2.imread(image)
    y,x = img.shape[:2]

    if x % 2 != 0:
       x += 1

    if y % 2 != 0:
       y += 1

    x_center = int(x/2)
    y_center = int(y/2)
    
    cut_image = img[y_center - 200:y_center + 200, x_center - 200:x_center + 200]
    cv2.imwrite("images/small_cat.jpg", cut_image)
    cv2.imshow('original_image', img)
    cv2.imshow('cut_image', cut_image)


if __name__ == '__main__':
    image_centering('images/variant-8.jpg')

cv2.waitKey(0)
cv2.destroyAllWindows()