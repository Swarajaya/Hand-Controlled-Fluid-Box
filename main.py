import cv2
from fluid import Fluid, WIDTH, HEIGHT
from hand_tracking import HandTracker

def main():
    cap = cv2.VideoCapture(0)
    cap.set(3, WIDTH)
    cap.set(4, HEIGHT)

    fluid = Fluid()
    hand = HandTracker()

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)

        # Get hand gesture data
        hand_data = hand.get_gestures(frame, WIDTH, HEIGHT)

        # Update fluid system
        fluid.step(hand_data)

        # Draw fluid + container
        fluid.draw(frame)

        # Debug visuals (optional, helps learning)
        if hand_data is not None:
            cx, cy = hand_data["pos"].astype(int)
            cv2.circle(frame, (cx, cy), 8, (255, 0, 0), -1)

        cv2.putText(
            frame,
            "Hand Controlled Fluid Box",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (255, 255, 255),
            2
        )

        cv2.imshow("Fluid Simulation", frame)

        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
