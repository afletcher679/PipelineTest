# PipelineTest
### Included in PipelineTest:
    - WpfApp called Greetings. Its a simple WpfApp that shows "Hello!" or "Goodbye!" messages after clicking display, based on the selected button.
    - 3 Automated Python Tests using unittest and pyautogui libraries (PipelineTest\PipelineWpfApp\PythonTests)
        - test_1: simple test that always passes just to prove that a pipeline could pass or fail based on the test result
        - test_app_opens: this has 2 tests within it: test_app_opens and test_select_goodbye_see_message
            - test_app_opens opens the app and verifies there is 1 window open with the title "Greetings"
            - test_select_goodbye_see_message locates and clicks the goodbye option, clicks display, and verifies the "Goodbye!" message shows
    - Screenshots of the necessary components for testing with pyautogui
    - The .exe for the WpfApp (PipelineTest\WpfAppExe). You need the whole folder to run the app

### To run the tests:
    1. Open the solution(PipelineWpfApp.sln) in Visual Studio
    2. Make sure to change line 19 of test_app_opens.py to the location of the executable
    3. Verify that the local_images_dir or testing_images_dir is set to where the wpfApp_screenshots folder is located. The program is currently using testing_images_dir
    4. In Visual Studio in the Test Explorer, you will see the 3 tests and you can run them from there or command line "pytest [location of PythonTests folder]"