import cv2
import numpy as np
import mediapipe as mp

mp_pose = mp.solutions.pose
pose = mp_pose.Pose()
mp_drawing = mp.solutions.drawing_utils

def analyze_pose_from_image(image_bytes):
    # نحول الصورة من bytes إلى NumPy array
    nparr = np.frombuffer(image_bytes, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # نحلل الصورة باستخدام MediaPipe
    results = pose.process(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

    # لو في نتائج، نرجع النقاط
    if results.pose_landmarks:
        keypoints = []
        for lm in results.pose_landmarks.landmark:
            keypoints.append({
                "x": lm.x,
                "y": lm.y,
                "z": lm.z,
                "visibility": lm.visibility
            })
        return {
            "success": True,
            "keypoints": keypoints
        }
    else:
        return {
            "success": False,
            "message": "No pose detected"
        }
