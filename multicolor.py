import cv2
import numpy as np
import time
from tkinter import Tk, Label, Button, StringVar, OptionMenu, CENTER

# Global variable to store the selected color
selected_color = None

def create_background(cap, num_frames=30):
    print("Capturing background. Please move out of frame")
    backgrounds = []
    for i in range(num_frames):
        ret, frame = cap.read()
        if ret:
            backgrounds.append(frame.astype(np.float32))
        else:
            print(f"Warning: Could not read frame {i+1}/{num_frames}")
        time.sleep(0.1)
    if backgrounds:
        return np.median(backgrounds, axis=0).astype(np.uint8)
    else:
        raise ValueError("Could not capture frames for background")

def create_mask(frame, lower_color, upper_color):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_color, upper_color)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8), iterations=2)
    mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE, np.ones((3, 3), np.uint8), iterations=1)
    return mask

def apply_cloak_effect(frame, mask, background):
    mask_inv = cv2.bitwise_not(mask)
    fg = cv2.bitwise_and(frame, frame, mask=mask_inv)
    bg = cv2.bitwise_and(background, background, mask=mask)
    return cv2.add(fg, bg)

def select_color_window():
    global selected_color
    root = Tk()
    root.title("Choose Cloak Color")

    # Center the pop-up on the screen
    window_width, window_height = 400, 200
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    position_top = (screen_height // 2) - (window_height // 2)
    position_left = (screen_width // 2) - (window_width // 2)
    root.geometry(f"{window_width}x{window_height}+{position_left}+{position_top}")

    # Styling
    root.configure(bg="dark blue")
    color_var = StringVar(root)
    color_var.set("Select Color")  # Default option

    # Predefined cloak colors
    color_options = ["Red", "Sky Blue", "Bright Yellow", "Olive Green"]

    # Title Label
    Label(root, text="Choose a cloak color:", font=("Arial", 14), bg="white", fg="black", anchor=CENTER).pack(pady=10)

    # Dropdown menu
    OptionMenu(root, color_var, *color_options).pack(pady=10)

    # Submit button
    def on_submit():
        global selected_color
        selected_color = color_var.get()
        if selected_color != "Select Color":
            root.destroy()
        else:
            Label(root, text="Please select a valid color.", font=("Arial", 12), fg="red", bg="dark blue").pack()

    Button(root, text="Submit", command=on_submit, bg="white", fg="black", font=("Arial", 12)).pack(pady=10)
    root.mainloop()

def main():
    global selected_color
    select_color_window()

    if not selected_color:
        print("No color selected. Exiting.")
        return

    print(f"You have chosen: {selected_color}")

    # Predefined HSV ranges for colors
    colors = {
        "Red": {
            "lower": [np.array([0, 120, 70]), np.array([170, 120, 70])],
            "upper": [np.array([10, 255, 255]), np.array([180, 255, 255])]
        },
        "Sky Blue": {
            "lower": np.array([90, 50, 70]),
            "upper": np.array([110, 255, 255])
        },
        "Bright Yellow": {
            "lower": np.array([20, 120, 70]),
            "upper": np.array([30, 255, 255])
        },
        "Olive Green": {
            "lower": np.array([70, 50, 50]),
            "upper": np.array([85, 255, 255])
        }
    }

    # Get the HSV ranges for the selected color
    if selected_color == "Red":
        lower_color1, lower_color2 = colors[selected_color]["lower"]
        upper_color1, upper_color2 = colors[selected_color]["upper"]
    else:
        lower_color1 = colors[selected_color]["lower"]
        upper_color1 = colors[selected_color]["upper"]

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    try:
        background = create_background(cap)
    except ValueError as e:
        print(f"Error: {e}")
        cap.release()
        return

    print("Start main loop. Press 'q' to quit")
    cv2.namedWindow("Invisible Cloak", cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty("Invisible Cloak", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Could not read frame")
            time.sleep(1)
            continue

        if selected_color == "Red":
            # Combine the two ranges for red
            mask1 = create_mask(frame, lower_color1, upper_color1)
            mask2 = create_mask(frame, lower_color2, upper_color2)
            mask = cv2.add(mask1, mask2)
        else:
            mask = create_mask(frame, lower_color1, upper_color1)

        result = apply_cloak_effect(frame, mask, background)
        cv2.imshow("Invisible Cloak", result)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
