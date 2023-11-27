# [Checkbox Client Python](https://github.com/tapsterbot/checkbox-client-python)

Python client library for Tapster Checkbox

## To install:
  ```
  git clone https://github.com/tapsterbot/checkbox-client-python.git
  cd checkbox-client-python
  python3 -m venv env
  source env/bin/activate
  pip install -r requirements.txt
  ```


## To test with an interactive session (REPL):
  ```
  $ python -i test.py --host=http://checkboxmini.local:5000

  # Raw mouse move:
  # Uncalibrated/unsynced to pixel coordinates
  >>> m.raw.move_by(100,100)

  # Mouse click
  >>> m.click()

  # Mouse down (Press mouse button and hold it down)
  >>> m.down()

  # Mouse up (Release mouse button)
  >> m.up()

  # Go to a specific location using MouseKeys:
  # MouseKeys mouse movements have zero acceleration, so calls are consistent and accurate.
  >>> mk.move_to(100,100)

  # Type text:
  >>> k.type("yo")

  # Get a screenshot
  >>> s.get_screenshot() # saved locally as screenshot.jpeg

  >>> s.get_screenshot("image-001.jpeg") # saved locally as image-001.jpeg
  ```


## Setup for iOS (iPhone and iPad)

### Enable Assistive Touch:
  ```
  Settings > Accessibility > Touch
  Select AssistiveTouch
  Slide AssistiveTouch toggle right to enable
  Slide "Perform Touch Gestures" toggle right to enable
  Set "Tracking Sensitivity" min to the left (turtle icon)
  ```


### Control the Pointer with the External Keyboard
  ```
  Settings > Accessibility > Touch
  Select AssistiveTouch
  Select MouseKeys
  Slide the MouseKeys toggle right to enable
  Slide "Use Primary Keyboard" toggle left to disable
  Set "Initial Delay" min to the left (turtle icon)
  Set "Maximum Speed" to center (equidistant from turtle and rabbit)
  ```

### Change Pointer Settings
  ```
  Settings > Accessibility > Pointer Control
  Slide the "Increase Contrast" toggle right to enable
  Slide the "Automatically Hide Pointer" toggle right to enable
  Set "Color" to None
  Set "Pointer Size" max to the right (largest)
  #Set "Scrolling Speed" max to the right (rabbit icon)
  ```
