import cv2
import mediapipe as mp
import time

mpDraw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose
pose = mpPose.Pose()
cap = cv2.VideoCapture('PoseVideo/1.mp4')
pTime = 0

# storing the pose landmarks of each person
pose_landmarks_list = []

while True:
    success, img = cap.read()
    if not success:
        break
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = pose.process(imgRGB)
    # print(results.pose_landmarks)
    if results.pose_landmarks:
        # Append the pose landmarks to the list
        pose_landmarks_list.append(results.pose_landmarks)

        # Drav the landmarks and circle for the first two people
        for i, landmarks in enumerate(pose_landmarks_list[:2]):
            mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)
            for id, lm in enumerate(results.pose_landmarks.landmark):
                h, w, c = img.shape
            # print(id, lm)
                cx, cy = int(lm.x * w), int(lm.y * h)
                cv2.circle(img, (cx, cy), 5, (0, 0, 255), cv2.FILLED)
    cTime = time.time()
    if cTime != pTime:
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3, 
                    (255, 0, 255), 3)
    cv2.imshow("image", img)
    cv2.waitKey(1)

cap.release()
cv2.destroyAllWindows()