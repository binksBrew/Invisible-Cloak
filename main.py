# import cv2
# import numpy as np
# import time
# import argparse


# def parse_args():
#     parser = argparse.ArgumentParser(description="Invisibility Cloak using OpenCV")
#     parser.add_argument('--color', type=str, default='red', choices=['red', 'blue', 'green'], help='Cloak color')
#     parser.add_argument('--bg_frames', type=int, default=60, help='Number of frames to capture background')
#     parser.add_argument('--output', type=str, default='output.avi', help='Output video filename')
#     return parser.parse_args()


# def get_color_bounds(color):
#     if color == 'red':
#         return [(np.array([0, 120, 50]), np.array([10, 255, 255])),
#                 (np.array([170, 120, 50]), np.array([180, 255, 255]))]
#     elif color == 'blue':
#         return [(np.array([100, 150, 0]), np.array([140, 255, 255]))]
#     elif color == 'green':
#         return [(np.array([40, 40, 40]), np.array([70, 255, 255]))]
#     else:
#         raise ValueError("Unsupported color")


# def capture_background(cap, num_frames):
#     print("[INFO] Capturing background. Please stay out of frame...")
#     bg_frames = []
#     for i in range(num_frames):
#         ret, frame = cap.read()
#         if not ret:
#             continue
#         frame = np.flip(frame, axis=1)
#         bg_frames.append(frame.copy())  # store clean frame

#         # Show live feedback without modifying stored frame
#         preview = frame.copy()
#         cv2.putText(preview, f"Capturing background... {i+1}/{num_frames}", (10, 30),
#                     cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
#         cv2.imshow("Background Capture", preview)
#         cv2.waitKey(1)
#         time.sleep(0.03)
#     cv2.destroyWindow("Background Capture")
#     return np.median(bg_frames, axis=0).astype(np.uint8)


# def create_mask(hsv, bounds):
#     mask = np.zeros(hsv.shape[:2], dtype=np.uint8)
#     for lower, upper in bounds:
#         mask |= cv2.inRange(hsv, lower, upper)

#     kernel = np.ones((3, 3), np.uint8)
#     mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=2)
#     mask = cv2.dilate(mask, kernel, iterations=1)
#     return mask


# def invisibility_cloak(args):
#     cap = cv2.VideoCapture(0)
#     if not cap.isOpened():
#         raise RuntimeError("Webcam not accessible.")

#     width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
#     height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
#     fps = int(cap.get(cv2.CAP_PROP_FPS)) or 20

#     out = cv2.VideoWriter(args.output, cv2.VideoWriter_fourcc(*'XVID'), fps, (width, height))
#     color_bounds = get_color_bounds(args.color)

#     background = capture_background(cap, args.bg_frames)
#     print("[INFO] Background captured. Cloak effect starting...")

#     while True:
#         ret, frame = cap.read()
#         if not ret:
#             break

#         frame = np.flip(frame, axis=1)
#         hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

#         mask = create_mask(hsv, color_bounds)
#         inv_mask = cv2.bitwise_not(mask)

#         fg = cv2.bitwise_and(frame, frame, mask=inv_mask)
#         bg = cv2.bitwise_and(background, background, mask=mask)
#         final = cv2.add(fg, bg)

#         out.write(final)
#         cv2.imshow("Invisibility Cloak", final)

#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

#     cap.release()
#     out.release()
#     cv2.destroyAllWindows()
#     print("[INFO] Cloak session ended. Output saved.")


# if __name__ == "__main__":
#     args = parse_args()
#     try:
#         invisibility_cloak(args)
#     except Exception as e:
#         print(f"[ERROR] {e}")













import cv2
import numpy as np
import time
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def get_color_bounds(color):
    if color == 'red':
        return [(np.array([0, 120, 50]), np.array([10, 255, 255])),
                (np.array([170, 120, 50]), np.array([180, 255, 255]))]
    elif color == 'blue':
        return [(np.array([100, 150, 0]), np.array([140, 255, 255]))]
    elif color == 'green':
        return [(np.array([40, 40, 40]), np.array([70, 255, 255]))]
    else:
        raise ValueError("Unsupported color")


def capture_background(cap, num_frames):
    print("[INFO] Capturing background. Please stay out of frame...")
    bg_frames = []
    for i in range(num_frames):
        ret, frame = cap.read()
        if not ret:
            continue
        frame = np.flip(frame, axis=1)
        bg_frames.append(frame.copy())

        preview = frame.copy()
        cv2.putText(preview, f"Capturing background... {i+1}/{num_frames}", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        cv2.imshow("Background Capture", preview)
        cv2.waitKey(1)
        time.sleep(0.03)
    cv2.destroyWindow("Background Capture")
    return np.median(bg_frames, axis=0).astype(np.uint8)


def create_mask(hsv, bounds):
    mask = np.zeros(hsv.shape[:2], dtype=np.uint8)
    for lower, upper in bounds:
        mask |= cv2.inRange(hsv, lower, upper)

    kernel = np.ones((3, 3), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=2)
    mask = cv2.dilate(mask, kernel, iterations=1)
    return mask


def invisibility_cloak(color, bg_frames, output):
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        messagebox.showerror("Error", "Webcam not accessible.")
        return

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS)) or 20

    out = cv2.VideoWriter(output, cv2.VideoWriter_fourcc(*'XVID'), fps, (width, height))
    color_bounds = get_color_bounds(color)

    background = capture_background(cap, bg_frames)
    print("[INFO] Background captured. Cloak effect starting...")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = np.flip(frame, axis=1)
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        mask = create_mask(hsv, color_bounds)
        inv_mask = cv2.bitwise_not(mask)

        fg = cv2.bitwise_and(frame, frame, mask=inv_mask)
        bg = cv2.bitwise_and(background, background, mask=mask)
        final = cv2.add(fg, bg)

        out.write(final)
        cv2.imshow("Invisibility Cloak", final)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()
    print("[INFO] Cloak session ended. Output saved.")


# -------- GUI Setup --------
def start_cloak():
    color = color_var.get()
    try:
        bg_frames = int(bg_frames_var.get())
        output = output_var.get().strip() or "output.avi"

        if not output.endswith('.avi'):
            output += '.avi'

        invisibility_cloak(color, bg_frames, output)
    except Exception as e:
        messagebox.showerror("Error", str(e))


root = tk.Tk()
root.title("Invisibility Cloak GUI")
root.geometry("350x320")
root.resizable(False, False)

tk.Label(root, text="Select Cloak Color:").pack(pady=5)
color_var = tk.StringVar(value='red')
ttk.Combobox(root, textvariable=color_var, values=['red', 'blue', 'green'], state='readonly').pack()

tk.Label(root, text="Background Frames:").pack(pady=5)
bg_frames_var = tk.IntVar(value=60)
tk.Scale(root, from_=10, to=120, orient=tk.HORIZONTAL, variable=bg_frames_var).pack()

tk.Label(root, text="Output Filename:").pack(pady=5)
output_var = tk.StringVar(value="output.avi")
tk.Entry(root, textvariable=output_var, width=30).pack()

tk.Button(root, text="Start Cloak", command=start_cloak, bg="green", fg="white").pack(pady=20)

tk.Label(root, text="Press 'q' to quit cloak mode", fg="gray").pack()

root.mainloop()
