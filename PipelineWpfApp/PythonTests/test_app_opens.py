import unittest
import subprocess
import pyautogui
import pygetwindow
import time
import os

windows = []
parent_dir = os.path.dirname(os.getcwd())
images_dir = os.path.join(parent_dir, 'wpfApp_screenshots')


class TestAppUi(unittest.TestCase):

    @staticmethod
    def start_app():
        subprocess.Popen('C:\\Users\\tester\\Desktop\\PipelineTest\\drop\\PipelineWpfApp.exe')
        time.sleep(3)
        global windows
        windows = pygetwindow.getWindowsWithTitle("Greetings")
        matching_windows = len(windows)
        if matching_windows == 1:
            return True
        elif matching_windows > 1:
            while matching_windows != 1:
                windows[matching_windows - 1].close()
                windows = pygetwindow.getWindowsWithTitle("Greetings")
                matching_windows = len(windows)
            return True

    def test_app_opens(self):
        window_open = self.start_app()
        self.assertTrue(window_open)

    @staticmethod
    def move_window_to_start_position():
        window = windows[0]
        window.moveTo(100, 100)

    def find_image_90_confidence(self, image_path):
        try:
            x, y = pyautogui.locateCenterOnScreen(image_path, confidence=0.9)
            return x, y
        except pyautogui.ImageNotFoundException:
            print(f'{image_path} could not be found with 90% confidence.')
            self.fail(f'{image_path} could not be found with 90% confidence.')

    def get_display_button_position(self):
        display_button_image_path = os.path.join(images_dir, 'display_button.PNG')
        x, y = self.find_image_90_confidence(display_button_image_path)
        return x, y

    def get_goodbye_button_position(self):
        goodbye_image_path = os.path.join(images_dir, 'goodbye_unselected.PNG')
        x, y = self.find_image_90_confidence(goodbye_image_path)
        return x, y

    @staticmethod
    def get_screen_res():
        print(pyautogui.size())

    def test_select_goodbye_see_message(self):
        self.test_app_opens()
        self.move_window_to_start_position()

        goodbye_select_position = self.get_goodbye_button_position()
        pyautogui.click(goodbye_select_position[0], goodbye_select_position[1])

        display_button_position = self.get_display_button_position()
        pyautogui.click(display_button_position[0], display_button_position[1])

        goodbye_image_path = os.path.join(images_dir, 'goodbye_message.PNG')
        result = pyautogui.locateOnWindow(goodbye_image_path, 'Greetings', confidence=0.9)
        self.assertIsNotNone(result)


if __name__ == '__main__':
    unittest.main()
