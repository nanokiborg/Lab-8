import numpy as np
import cv2

# Вариант №8

def video_processing():
    cap = cv2.VideoCapture(0)
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        height, width = frame.shape[:2] 

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
        gray = cv2.GaussianBlur(gray, (9, 9), 0)

        # используем метод для поиска круга
        circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, dp=1.2, 
                                   minDist=100, param1=80, param2=40,
                                   minRadius=30, maxRadius=250)
        if circles is not None:
            circles = np.uint16(np.around(circles)) 
            x, y, r = circles[0, 0] 

            # рисуем линии и круг треккинга
            cv2.circle(frame, (x, y), r, (0, 0, 255), 3)
            cv2.line(frame, (x, 0), (x, height), (255, 0, 0), 2)
            cv2.line(frame, (0, y), (width, y), (255, 0, 0), 2)
            cv2.circle(frame, (x, y), 2, (0, 255, 0), 3)

            print(f"Координаты центра: ({x}, {y})")

        cv2.imshow('Tracking', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    
    video_processing()

