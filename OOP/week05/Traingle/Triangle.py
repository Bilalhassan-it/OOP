class Triangle:
    object_counter = 0  # Class variable

    def __init__(self, sideA=1.0, sideB=1.0, sideC=1.0):
        self._sideA = sideA
        self._sideB = sideB
        self._sideC = sideC
        Triangle.object_counter += 1  # Increment object counter

    # --- Properties for sides ---
    @property
    def sideA(self):
        return self._sideA

    @sideA.setter
    def sideA(self, value):
        self._sideA = value

    @property
    def sideB(self):
        return self._sideB

    @sideB.setter
    def sideB(self, value):
        self._sideB = value

    @property
    def sideC(self):
        return self._sideC

    @sideC.setter
    def sideC(self, value):
        self._sideC = value

    # --- Class method to get object count ---
    @classmethod
    def objectCount(cls):
        return cls.object_counter

    # --- Instance methods ---
    def perimeter(self):
        return self.sideA + self.sideB + self.sideC

    def isRightAngled(self):
        a, b, c = sorted([self.sideA, self.sideB, self.sideC])
        return abs(a**2 + b**2 - c**2) < 1e-9

    def __str__(self):
        return f"Triangle sides: {self.sideA}, {self.sideB}, {self.sideC}"


