import pytest
from rectangle import Rectangle
# test function to be executed by PyTest
class TestGetAreaRectangle:
    # @pytest.fixture
    # def rectangle():
    #     return Rectangle(0, 0)

    def test_normal_case(self):
        rectangle = Rectangle(2, 3)
        assert rectangle.get_area() == 6, "incorrect area"

    def test_negative_case(rectangle):
        """expect -1 as output to denote error when looking at
        negative area"""
        rectangle = Rectangle(-1, 2)
        assert rectangle.get_area() == -1,"incorrect negative output"


