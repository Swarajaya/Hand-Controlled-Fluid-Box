import mediapipe as mp
import numpy as np
import math

class HandTracker:
    def __init__(self):
        self.hands = mp.solutions.hands.Hands(
            max_num_hands=1,
            min_detection_confidence=0.6,
            min_tracking_confidence=0.6
        )

    def get_gestures(self, frame, w, h):
        rgb = frame[:, :, ::-1]
        res = self.hands.process(rgb)

        if not res.multi_hand_landmarks:
            return None

        lm = res.multi_hand_landmarks[0].landmark

        # Finger position
        index = np.array([lm[8].x * w, lm[8].y * h])
        thumb = np.array([lm[4].x * w, lm[4].y * h])

        # Pinch distance (resize)
        pinch_dist = np.linalg.norm(index - thumb)

        # Rotation angle (wrist → index base)
        wrist = np.array([lm[0].x * w, lm[0].y * h])
        index_base = np.array([lm[5].x * w, lm[5].y * h])
        angle = math.atan2(index_base[1] - wrist[1],
                           index_base[0] - wrist[0])

        return {
            "pos": index,
            "pinch": pinch_dist,
            "angle": angle
        }
