# This class models a simple sensor object.
# Each sensor has an id, a location, and an "active" status.
class Sensor:
    # The constructor runs when we create a new Sensor.
    # Parameters become starting values for this object's attributes.
    def __init__(self, sensor_id: str, location: str, is_active: bool):
        # "self" means "this specific object".
        # These assignments store data inside the object.
        self.sensor_id = sensor_id
        self.location = location
        self.is_active = is_active

    # Turn the sensor on by setting its active state to True.
    def activate(self) -> None:
        self.is_active = True

    # Turn the sensor off by setting its active state to False.
    def deactivate(self) -> None:
        self.is_active = False

    # __str__ controls how the object appears when printed.
    # Returning a string here makes print(sensor) readable.
    def __str__(self) -> str:
        return f"{self.sensor_id} at {self.location}, active={self.is_active}"


# MeasurementSensor is a child class of Sensor.
# It inherits sensor_id, location, is_active, activate(), deactivate(), and __str__().
# Then it adds two new attributes (value, units) and one new method (update_value).
class MeasurementSensor(Sensor):
    # This constructor first calls Sensor's constructor with super().__init__().
    # Then it stores the measurement-specific data.
    def __init__(self, sensor_id: str, location: str, is_active: bool, value: float, units: str):
        super().__init__(sensor_id, location, is_active)
        self.value = value
        self.units = units

    # Update the numeric reading stored in this sensor.
    def update_value(self, new_value: float) -> None:
        self.value = new_value

    # Reuse Sensor's __str__() and append measurement information.
    def __str__(self) -> str:
        return super().__str__() + f", value={self.value} {self.units}"


def main() -> None:
    measurement = MeasurementSensor("M-201", "Lab B", True, 22.5, "C")
    print("Measurement initial:", measurement)

    # Child class can still use inherited methods.
    measurement.deactivate()
    print("Measurement after deactivate:", measurement)

    measurement.activate()
    print("Measurement after activate:", measurement)

    # Child-specific method updates the stored reading.
    measurement.update_value(23.1)
    print("Measurement after update_value:", measurement)


if __name__ == "__main__":
    main()
