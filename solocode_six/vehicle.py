class Vehicle:
    def __init__(self, name, fuel_capacity, cost_per_gallon, miles_per_gallon):
        self._name = name
        self._fuel_capacity = fuel_capacity
        self._cost_per_gallon = cost_per_gallon
        self._miles_per_gallon = miles_per_gallon

    @property
    def range(self) -> float:
        return self._fuel_capacity * self._miles_per_gallon

    @property
    def cost_per_mile(self) -> float:
        return self._cost_per_gallon / self._miles_per_gallon
