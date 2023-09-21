class Car():
    def __init__(self):
        self._seat = None

    @property # getter
    def seat(self):
        return self._seat

    @seat.setter # setter
    def seat(self, seat):
        self._seat = seat 

c = Car()
c.seat = 6
print(c.seat)
