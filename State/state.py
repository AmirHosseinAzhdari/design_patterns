"""State (Behavior)

Changes the behavior of a piece of code based on the modes for which it occurs

"""


class State:
    def operate(self):
        print(f"Turning TV {self.status}")


class TurnOn(State):
    def __init__(self, tv):
        self._tv = tv
        self.status = "On"

    def change_state(self):
        self._tv.state = self._tv.off


class TurnOff(State):
    def __init__(self, tv):
        self._tv = tv
        self.status = "Off"

    def change_state(self):
        self._tv.state = self._tv.on


class TV:
    def __init__(self) -> None:
        self.on = TurnOn(self)
        self.off = TurnOff(self)
        self.state = self.on

    def press(self):
        self.state.operate()
        self.state.change_state()


t = TV()

t.press()
t.press()
t.press()
t.press()
