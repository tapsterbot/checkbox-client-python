import json
import requests
from typing import List
from requests.compat import urljoin

# Default host:
HOST = "http://localhost:5000"

class Ping:
    def __init__(self, host = HOST):
        self._host = host

    def ping(self, host = HOST):
        """
        Ping server

        Command line equivalent:
        $ curl $HOST/api/ping
        """
        url = urljoin(self._host, "/api/ping")
        print(url)
        response = requests.get(url)

        return response.json()

class Video:
    def __init__(self, host = HOST):
        self._host = host

    def config(self, host = HOST):
        """
        Config video by cropping image to phone outline

        Command line equivalent:
        $ curl $HOST/api/config/video/camera
        """
        url = urljoin(self._host, "/api/config/video/camera")
        response = requests.post(url)


class Config:
    def __init__(self, host = HOST):
        self._host = host

    def mouse_position(self):
        """
        Get mouse position

        Command line equivalent:
        $ curl $HOST/api/config/mouse/position
        """
        url = urljoin(self._host, "/api/config/mouse/position")
        response = requests.get(url)

        return response.json()

    def mouse_screen_position(self):
        """
        Get mouse position as screen coordinates

        Command line equivalent:
        $ curl $HOST/api/config/mouse/screen-position
        """
        url = urljoin(self._host, "/api/config/mouse/screen-position")
        response = requests.get(url)

        return response.json()

class Keyboard:
    def __init__(self, host = HOST):
        self._host = host

    def type(self, text = ""):
        """
        Type text

        Command line equivalent:
        $ curl -X POST $HOST/api/keyboard/type \
            -H "Content-Type: application/json" \
            -d '{"text": "yo"}'
        """
        url = urljoin(self._host, "/api/keyboard/type")
        payload = {'text': text}
        response = requests.post(url, json = payload)

    def press(self, modifiers: List[int], key: int = 0):
        """
        Type text

        Command line equivalent:
        (Send Shift + Tab)
        $ curl -X POST $HOST/api/keyboard/press \
            -H "Content-Type: application/json" \
            -d '{"modifiers": [2], "key": 43}'
        """
        url = urljoin(self._host, "/api/keyboard/press")
        payload = {'modifiers': modifiers, 'key': key}
        response = requests.post(url, json = payload)



class RawMouse:
    def __init__(self, host = HOST):
        self._host = host

    def move_by(self, x = 0, y = 0):
        """
        Move x, y pixels

        Command line equivalent:
        $ curl -X POST $HOST/api/raw/mouse/move/by \
            -H "Content-Type: application/json" \
            -d '{"x": 0, "y": 0}'
        """
        url = urljoin(self._host, "/api/raw/mouse/move/by")
        payload = {'x': x, 'y': y}
        response = requests.post(url, json = payload)

    def drag(self, x = 0, y = 0):
        """
        Drag x, y pixels

        Command line equivalent:
        $ curl -X POST $HOST/api/raw/mouse/drag/by \
            -H "Content-Type: application/json" \
            -d '{"x": 0, "y": 0}'
        """
        url = urljoin(self._host, "/api/raw/mouse/drag/by")
        payload = {'x': x, 'y': y}
        response = requests.post(url, json = payload)

    def swipe_up(self):
        """
        Swipe up

        Command line equivalent:
        $ curl -X POST $HOST/api/raw/mouse/swipe/up \
            -H "Content-Type: application/json"
        """
        url = urljoin(self._host, "/api/raw/mouse/swipe/up")
        response = requests.post(url)

    def swipe_down(self):
        """
        Swipe down

        Command line equivalent:
        $ curl -X POST $HOST/api/raw/mouse/swipe/down \
            -H "Content-Type: application/json"
        """
        url = urljoin(self._host, "/api/raw/mouse/swipe/down")
        response = requests.post(url)

    def swipe_left(self):
        """
        Swipe left

        Command line equivalent:
        $ curl -X POST $HOST/api/raw/mouse/swipe/left \
            -H "Content-Type: application/json"
        """
        url = urljoin(self._host, "/api/raw/mouse/swipe/left")
        response = requests.post(url)

    def swipe_right(self):
        """
        Swipe right

        Command line equivalent:
        $ curl -X POST $HOST/api/raw/mouse/swipe/right \
            -H "Content-Type: application/json"
        """
        url = urljoin(self._host, "/api/raw/mouse/swipe/right")
        response = requests.post(url)

class Mouse:
    """
    Example Usage:
    >>> from checkbox import Mouse
    >>> m = Mouse()
    >>> m.home()
    """
    def __init__(self, host = HOST):
        self._host = host
        self.x = 0
        self.y = 0
        self.calibrated = False
        self.raw = RawMouse(host)

    def jiggle(self):
        """
        Jiggle the mouse

        Command line equivalent:
        $ curl $HOST/api/mouse/jiggle
        """
        url = urljoin(self._host, "/api/mouse/jiggle")
        response = requests.get(url)

    def down(self):
        """
        Send a mouseDown event

        Command line equivalent:
        $ curl -X POST $HOST/api/mouse/down \
            -H "Content-Type: application/json"
        """
        url = urljoin(self._host, "/api/mouse/down")
        response = requests.post(url)

    def up(self):
        """
        Send a mouseUp event

        Command line equivalent:
        $ curl -X POST $HOST/api/mouse/up \
            -H "Content-Type: application/json"
        """
        url = urljoin(self._host, "/api/mouse/up")
        response = requests.post(url)

    def click(self):
        """
        Shortcut for down(), up()

        Command line equivalent:
        $ curl -X POST $HOST/api/mouse/click -H "Content-Type: application/json"
        """
        url = urljoin(self._host, "/api/mouse/click")
        response = requests.post(url)

    def move_by(self, x = 0, y = 0):
        """
        Move x, y pixels

        Command line equivalent:
        $ curl -X POST $HOST/api/mouse/move/by \
            -H "Content-Type: application/json" \
            -d '{"x": 0, "y": 0}'
        """
        url = urljoin(self._host, "/api/mouse/move/by")
        payload = {'x': x, 'y': y}
        response = requests.post(url, json = payload)

    def home(self):
        """
        Move mouse home

        Command line equivalent:
        $ curl -X POST $HOST/api/mouse/move/home -H "Content-Type: application/json"
        """
        url = urljoin(self._host, "/api/mouse/move/home")
        response = requests.post(url)
        #self.x = 40
        #self.y = 40
        # Mouse position should now logically be (x=40, y=40)

class RawMouseKeys:
    def __init__(self, host = HOST):
        self._host = host

    def move_by(self, x = 0, y = 0):
        """
        Move x, y pixels

        Command line equivalent:
        $ curl -X POST $HOST/api/raw/mouse-keys/move/by \
            -H "Content-Type: application/json" \
            -d '{"x": 0, "y": 0}'
        """
        url = urljoin(self._host, "/api/raw/mouse-keys/move/by")
        payload = {'x': x, 'y': y}
        response = requests.post(url, json = payload)

    def drag(self, x = 0, y = 0):
        """
        Drag x, y pixels

        Command line equivalent:
        $ curl -X POST $HOST/api/raw/mouse-keys/drag/by \
            -H "Content-Type: application/json" \
            -d '{"x": 0, "y": 0}'
        """
        url = urljoin(self._host, "/api/raw/mouse-keys/drag/by")
        payload = {'x': x, 'y': y}
        response = requests.post(url, json = payload)

class MouseKeys:
    """
    Example Usage:
    >>> from checkbox import MouseKeys
    >>> mk = MouseKeys()
    >>> mk.home()
    """
    def __init__(self, host = HOST):
        self._host = host
        self.x = 0
        self.y = 0
        self.calibrated = False
        self.raw = RawMouseKeys(host)

    def jiggle(self):
        """
        Jiggle the mouse

        Command line equivalent:
        $ curl $HOST/api/mouse/jiggle
        """
        url = urljoin(self._host, "/api/mouse-keys/jiggle")
        response = requests.get(url)

    def down(self):
        """
        Send a mouseDown event

        Command line equivalent:
        $ curl -X POST $HOST/api/mouse-keys/down \
            -H "Content-Type: application/json"
        """
        url = urljoin(self._host, "/api/mouse-keys/down")
        response = requests.post(url)

    def up(self):
        """
        Send a mouseUp event

        Command line equivalent:
        $ curl -X POST $HOST/api/mouse-keys/up \
            -H "Content-Type: application/json"
        """
        url = urljoin(self._host, "/api/mouse-keys/up")
        response = requests.post(url)

    def click(self):
        """
        Send a mouse click

        Command line equivalent:
        $ curl -X POST $HOST/api/mouse-keys/click \
            -H "Content-Type: application/json"
        """
        url = urljoin(self._host, "/api/mouse-keys/click")
        response = requests.post(url)

    def move_to(self, x = 0, y = 0):
        """
        Move x, y pixels

        Command line equivalent:
        $ curl -X POST $HOST/api/mouse-keys/move/to \
            -H "Content-Type: application/json" \
            -d '{"x": 0, "y": 0}'
        """
        url = urljoin(self._host, "/api/mouse-keys/move/to")
        payload = {'x': x, 'y': y}
        response = requests.post(url, json = payload)

    def home(self):
        """
        Move mouse home

        Command line equivalent:
        $ curl -X POST $HOST/api/mouse-keys/move/home \
            -H "Content-Type: application/json"
        """
        url = urljoin(self._host, "/api/mouse-keys/move/home")
        response = requests.post(url)
        self.x = 40
        self.y = 40
        # Mouse position should now logically be (x=40, y=40)

class Screenshot:
    def __init__(self, host = HOST):
        self._host = host

    def get_screenshot(self, filename = "screenshot.jpeg", format=""):
        """
        Type text

        Command line equivalent:
        $ curl $HOST/api/screenshot -o screenshot.jpeg
        $ curl $HOST/api/screenshot/gray -o screenshot.jpeg
        """
        if format == "gray":
            url = urljoin(self._host, "/api/screenshot/gray")
        else:
            url = urljoin(self._host, "/api/screenshot")
        response = requests.get(url)
        file = open(filename, "wb")
        file.write(response.content)
        file.close()
