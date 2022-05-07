from PIL import ImageGrab
from pynput import keyboard

def screen_shot():
    screenshot = ImageGrab.grab()
    screenshot.save('screenshot.jpg')
    
    
def press(key):
    try:
        if key == keyboard.Key.shift:
            print("アルファベット{0}が押されました".format(key.char))
    except AttributeError:
        if key == keyboard.Key.shift:
            screen_shot()

def release(key):
    if key == keyboard.Key.esc:
        return False

listener = keyboard.Listener(
    on_press = press,
    on_release = release
)
listener.start()