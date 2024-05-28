from pynput import keyboard, mouse
import threading
import time

# Global variables to control the program
running = False
stop_key = keyboard.Key.f8  # You can change this to any special key you prefer

def on_key_press(key):
    global running
    if key == stop_key:
        if running:
            running = False
            print("Program stopped.")
        else:
            running = True
            print("Program started.")

def mouse_click():
    global running
    while True:
        if running:
            mouse.Controller().click(mouse.Button.left, 1)
            

# Start the keyboard listener
keyboard_listener = keyboard.Listener(on_press=on_key_press)
keyboard_listener.start()

# Start the mouse click thread
mouse_thread = threading.Thread(target=mouse_click)
mouse_thread.start()

# Keep the main thread running
mouse_thread.join()
