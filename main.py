import cv2

cap = cv2.VideoCapture(0)  # Open the default camera (index 0)

while True:
    ret, frame = cap.read()  # Read a frame from the camera

    if not ret:
        print("Failed to capture frame from webcam.")
        break

    cv2.imshow('Webcam', frame)  # Display the frame in a window named 'Webcam'

    if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to exit
        break

cap.release()  # Release the camera
cv2.destroyAllWindows()  # Close all windows