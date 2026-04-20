# -------------------------------------------------------------
# Point and LabeledPoint --- Inheritance Demonstration
#
# This file shows a simple two-class hierarchy:
#
#   Point          <-- parent class (base class)
#   LabeledPoint   <-- child class (derived class)
#
# Key ideas to notice:
#   1. LabeledPoint inherits everything from Point.
#   2. super().__init__() lets the child reuse the parent constructor.
#   3. __str__ is overridden in the child to extend the parent's version.
# -------------------------------------------------------------


# --- Parent class -------------------------------------------
class Point:
    """Represents a 2-D point with x and y coordinates."""

    def __init__(self, x: float, y: float):
        # Store x and y as instance attributes.
        # Every Point object will have its own copies of these.
        self.x = x
        self.y = y

    def __str__(self) -> str:
        # Called automatically when we use print() on a Point object.
        return f"Point({self.x}, {self.y})"


# --- Child class --------------------------------------------
# LabeledPoint inherits from Point, indicated by (Point) here.
# That means LabeledPoint automatically has x, y, and __str__
# from Point --- we only need to add whatever is new.
class LabeledPoint(Point):
    """A Point that also carries a text label."""

    def __init__(self, x: float, y: float, label: str):
        # super() refers to the parent class (Point).
        # Calling super().__init__() runs Point's constructor,
        # which sets self.x and self.y.  We do NOT duplicate that code here.
        super().__init__(x, y)

        # Now add the attribute that is unique to LabeledPoint.
        self.label = label

    def __str__(self) -> str:
        # We want to build on Point's string representation, not replace it.
        # super().__str__() gives us "Point(x, y)", and we append the label.
        return super().__str__() + f" [{self.label}]"


# --- Demo ---------------------------------------------------
def main() -> None:
    # Create a plain Point object.
    p1 = Point(1.0, 2.0)
    print(p1)  # prints: Point(1.0, 2.0)

    # Create a LabeledPoint object.
    # It stores x, y (from Point) AND label (added by LabeledPoint).
    p2 = LabeledPoint(3.0, 4.0, "A")
    print(p2)  # prints: Point(3.0, 4.0) [A]


if __name__ == "__main__":
    main()
