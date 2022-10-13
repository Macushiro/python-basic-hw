"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""
class LowFuelError(Exception):
    def __init__(self, message="Not enough fuel to start car."):
        super().__init__(message)


class NotEnoughFuel(Exception):
    def __init__(self, message="Not enough fuel to reach finish point of route."):
        super().__init__(message)


class CargoOverload(Exception):
    def __init__(self, message="The vehicle is overload, we cannot move."):
        super().__init__(message)
