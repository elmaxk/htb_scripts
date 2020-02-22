
class CounterState:
    def __init__(self, step):
        self.step = step

    def __next__(self):
        """Move the counter step towards 0 by 1."""
        if self.step <= 0:
            raise StopIteration
        self.step -= 1
        return self.step


class Countdown:
    def __init__(self, steps):
        self.steps = steps

    def __iter__(self):
        """Return the iterator itself."""
        return CounterState(self.steps)