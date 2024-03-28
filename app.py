import cv2
import time

# Load the pre-trained face and eye cascade classifiers
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# Initialize the webcam
cap = cv2.VideoCapture(0)

# Create an empty list to store previous eye positions
prev_eye_positions = []

# Set the initial window size
cv2.namedWindow('Eye Movement Detection', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Eye Movement Detection', 800, 600)  # Adjust the size as needed

# Initialize a timer variable
timer = 5

while True:
    # Capture a frame from the webcam
    ret, frame = cap.read()

    if not ret:
        break  # If no frame is captured, exit the loop

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray)

    eyes_closed = True  # Assume eyes are closed until detected open

    for (x, y, w, h) in faces:
        # Draw a rectangle around the detected face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # Crop the region of interest (ROI) for eye detection
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]

        # Detect eyes in the ROI
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            # Draw a rectangle around the detected eye
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

            # Calculate the center of the detected eye
            eye_center = (x + ex + ew // 2, y + ey + eh // 2)

            # Store the eye center in the list
            prev_eye_positions.append(eye_center)

            # Limit the list to a certain number of previous positions
            max_positions = 10
            if len(prev_eye_positions) > max_positions:
                prev_eye_positions.pop(0)

            # Draw lines to connect previous eye positions
            for i in range(1, len(prev_eye_positions)):
                cv2.line(frame, prev_eye_positions[i - 1], prev_eye_positions[i], (0, 0, 255), 2)

            eyes_closed = False  # Eyes detected open
            timer = 5  # Reset the timer if a face is detected

    # Display a message in red if eyes are closed or not looking at the screen
    if eyes_closed:
        cv2.putText(frame, "Eyes Closed or Not Looking at Screen", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    else:
        cv2.putText(frame, "Eyes Open and Looking at Screen", (20, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Display the timer
    cv2.putText(frame, f"Timer: {timer}", (20, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # Decrement the timer if it's greater than 0
    if timer > 0:
        timer -= 1

    # If the timer reaches 0, capture a picture and store it with a timestamp
    if timer == 0:
        timestamp = time.strftime("%Y%m%d%H%M%S")
        image_filename = f'snapshot_{timestamp}.png'
        cv2.imwrite(image_filename, frame)
        print(f"Snapshot saved as '{image_filename}'")
        timer = 2  # Set the timer to 2 seconds for the next snapshot

    # Display the video frame
    cv2.imshow('Eye Movement Detection', frame)

    # Exit the loop if the 'q' key is pressed
    if cv2.waitKey(1000) & 0xFF == ord('q'):
        break

# Release the webcam and close the window
cap.release()
cv2.destroyAllWindows()
