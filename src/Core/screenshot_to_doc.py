import datetime
from PIL import ImageGrab
import numpy as np
import cv2
from pynput.mouse import Listener
from docx import Document
from docx.shared import Inches
import os


class ScreenshotToDoc:
    def __init__(self):
        self.doc = Document()
        self.screenshot_counter = 0
        self.screenshot_files = []
        self.listener = None

    def on_click(self, x, y, button, pressed):
        if pressed and button.name == 'left':
            # Capture screenshot
            img = ImageGrab.grab()
            img_np = np.array(img)
            img_final = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)

            # Save screenshot as image file
            time_stamp = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
            screenshot_file = f'{time_stamp}.png'
            cv2.imwrite(screenshot_file, img_final)
            self.screenshot_files.append(screenshot_file)

            # Add screenshot to Word document
            self.doc.add_picture(screenshot_file, width=Inches(6))
            self.screenshot_counter += 1

            print(f'Screenshot {self.screenshot_counter} captured and added to document.')

    def start(self):
        self.listener = Listener(on_click=self.on_click)
        self.listener.start()
        print("Screenshot capturing started. Click the left mouse button to capture screenshots.")

    def stop(self):
        self.listener.stop()
        self.save_and_cleanup()
        self.listener = None

    def save_and_cleanup(self):
        print('Stopping screenshot capture and saving document...')
        # Save the document
        self.doc.save('screenshots.docx')
        print('Document saved as screenshots.docx')

        # Delete the image files
        for file in self.screenshot_files:
            if os.path.exists(file):
                os.remove(file)
                print(f'Deleted {file}')
