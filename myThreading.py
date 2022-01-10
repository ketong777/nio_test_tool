import threading


class TimerRepeater(object):

    def __init__(self, name, interval, target):
        self._name = name
        self._thread = None
        self._event = None
        self._target = target
        self._interval = interval

    def _run(self):
        if self._interval != None:
            while not self._event.wait(self._interval):
                self._target()
        else:
            self._target()

    def start(self):
        if (self._thread == None):
            self._event = threading.Event()
            self._thread = threading.Thread(None, self._run, self._name)
            self._thread.start()

    def stop(self):
        if (self._thread != None):
            self._event.set()
            self._thread = None
