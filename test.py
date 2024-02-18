# 1. import your app
# from file 'app.py' import module 'app = Dash(__name__)'
from app import app

# 2. give each testcase a test case ID, and pass the fixture
# dash_duo as a function argument
def test_001_header_text_is_correct(dash_duo):
    # 3. host the app locally in a thread, all dash server configs could be passed after the first app argument
    dash_duo.start_server(app)

    # 4. use wait_for_* if your target element is the result of a callback,
    # keep in mind even the initial rendering can trigger callbacks
    dash_duo.wait_for_text_to_equal("#header", "Pink Morsel Sales Visualizer", timeout=10)

    # 5. use this form if its present is expected at the action point
    assert dash_duo.find_element("#header").text == "Pink Morsel Sales Visualizer"

    # Both #4 and #5 are doing the same check .
    #4 will wait for the expected state to be reached within a 10 seconds timeout.
    #5 find_element API call has an implicit global timeout of 2 seconds set at the driver level.
    # The API ```find_element('#header')``` is a shortcut to ```driver.find_element_by_css_selector('#header')```

def test_002_visualization_exists(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#visualizaion", timeout=10)

def test_region_picker_exists(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#region-picker", timeout=10)

# ----------------------- Instrcutions to run the tests --------------------------

# In order to avoid " 'chromedriver' executable needs to be in PATH." error when runing 'pytest' command. Do the following:

# 1. Download chromedriver: https://googlechromelabs.github.io/chrome-for-testing/#stable
# 2. Once unzipped. Do the following commands in your (venv) terminal:
# 3. Change your dir to where you downloaded and unzipped the chromedrive excutable file. In my case it is 'Users/adeliia/Downloads/chromedriver-mac=x64/chromedriver'
# cd /path/to/chromedriver/exicutable/file
# Run the executable chroemdriev file
#  ./chromedriver
# To confirm chromedrive now is runnig, you should see 'ChromeDriver was started successfully'. Don't close this tab in the terminal

# 4. Open another tab in the terminal. In this new tab do the following commands:
# 6. To Add chromedriver to PATH variable you have to add/copy the executable chromedriev file to one of the common directories, where executables are installed:
# 1) usr/local/bin
# 2) usr/bin
# 3) opt/
# sudo cp /path/to/chromedriver/exicutable/file /usr/local/bin

# 7. Confirm chromedrive is adedd to PATH
# chromedriver --version
# If chromedriver was successfully added to PATH variable, you should get a message like this: 'ChromeDriver XXX.X.XXXX.XXXX'

# 8. Run 'pytest' command to run all the files in current directory starting or ending with 'test'