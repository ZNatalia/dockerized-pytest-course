from scripts.chp2.video2.mapmaker_start import Point
import pytest


def test_make_one_point():
    p1 = Point("Dacar", 14.7167, 17.467)
    assert p1.get_lat_long() == (14.7167, 17.467)


def test_invalid_point_generaion():
    with pytest.raises(ValueError) as exp:
        Point("Bueno Aeros", 12.11386, -555.08269)
    assert(str(exp.value)) == "Invalid latitude, longitude combination"


def test_type_city_name_():
    with pytest.raises(Exception) as exp:
        Point(1, 14.7167, 17.467)
    assert(str(exp.value)) == "The name of the city is not a string"
