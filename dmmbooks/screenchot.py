from PIL import ImageGrab
from pynput import keyboard

def screen_shot():
    screenshot = ImageGrab.grab()
    screenshot.save('./screenshot.jpg')
    
    
def on_press(key):
    try:
        print("アルファベット{0}が押されました".format(key.char))
    # except AttributeError:        
    #     if key == keyboard.Key.shift:
    #         screen_shot()
    #         print('shift key pressed')
    except AttributeError:
        print('special key pressed: {0}'.format(
            key))

def on_release(key):
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()