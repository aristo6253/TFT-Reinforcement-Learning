import mss
import mss.tools
import time

bounding_box = {'top': 100, 'left': 100, 'width': 300, 'height': 300}

with mss.mss() as sct:
    for i in range(100):
        # screenshot = sct.grab(bounding_box)  # Take the screenshot of the primary monitor
        screenshot = sct.grab(sct.monitors[0])
        mss.tools.to_png(screenshot.rgb, screenshot.size, output=f'data/screenshots/screenshot_{i}.png')  # Save to the picture file
        time.sleep(1)
    