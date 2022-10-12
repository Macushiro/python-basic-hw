"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""
class LowFuelError(Exception):
    print("Not enough fuel to start car.")


class NotEnoughFuel(Exception):
    print("Not enough fuel to reach finish point of route.")


class CargoOverload(Exception):
    print("The vehicle is overload, we cannot move.")
