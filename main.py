import time
import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

FINGER_TIPS = [4, 8, 12, 16, 20]
FINGER_PIPS = [3, 6, 10, 14, 18]

def finger_states(hand_landmarks, handedness: str):
    lm = hand_landmarks.landmark
    states = []

    # Thumb: compare x direction based on handedness.
    if handedness.lower() == "right":
        states.append(lm[FINGER_TIPS[0]].x < lm[FINGER_PIPS[0]].x)
    else:
        states.append(lm[FINGER_TIPS[0]].x > lm[FINGER_PIPS[0]].x)

    # Other fingers: tip above PIP joint.
    for tip, pip in zip(FINGER_TIPS[1:], FINGER_PIPS[1:]):
        states.append(lm[tip].y < lm[pip].y)
    return states

def gesture_name(states):
    count = sum(states)
    if count == 0:
        return "Fist"
    if count == 5:
        return "Open palm"
    if states == [False, True, False, False, False]:
        return "Point"
    if states == [False, True, True, False, False]:
        return "Peace"
    return f"{count} fingers"

def main():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        raise RuntimeError("Could not open webcam.")

    prev = time.time()

    with mp_hands.Hands(
        static_image_mode=False,
        max_num_hands=2,
        min_detection_confidence=0.6,
        min_tracking_confidence=0.6
    ) as hands:
        while True:
            ok, frame = cap.read()
            if not ok:
                break

            frame = cv2.flip(frame, 1)
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            result = hands.process(rgb)

            if result.multi_hand_landmarks:
                for idx, hand_landmarks in enumerate(result.multi_hand_landmarks):
                    handedness = "Unknown"
                    if result.multi_handedness and idx < len(result.multi_handedness):
                        handedness = result.multi_handedness[idx].classification[0].label

                    states = finger_states(hand_landmarks, handedness)
                    label = f"{handedness}: {gesture_name(states)}"

                    mp_draw.draw_landmarks(
                        frame, hand_landmarks, mp_hands.HAND_CONNECTIONS
                    )

                    h, w = frame.shape[:2]
                    wrist = hand_landmarks.landmark[0]
                    x, y = int(wrist.x * w), int(wrist.y * h)
                    cv2.putText(
                        frame, label, (max(10, x - 40), max(30, y - 20)),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2
                    )

            now = time.time()
            fps = 1 / max(now - prev, 1e-6)
            prev = now
            cv2.putText(
                frame, f"FPS: {fps:.0f}", (18, 34),
                cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 255, 255), 2
            )

            cv2.imshow("Real-Time Hand Tracking", frame)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
