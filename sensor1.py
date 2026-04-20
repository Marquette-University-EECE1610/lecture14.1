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


def main() -> None:
    # Create one Sensor object. It starts inactive because we pass False.
    sensor = Sensor("S-101", "Lab A", False)

    print("Initial:", sensor)

    sensor.activate()
    print("After activate:", sensor)

    sensor.deactivate()
    print("After deactivate:", sensor)


if __name__ == "__main__":
    main()
