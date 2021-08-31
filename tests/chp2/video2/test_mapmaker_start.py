from scripts.chp2.video2.mapmaker_start import Point


def test_make_one_point():
    p1 = Point("Dacar", 14.7167, 17.467)
    assert p1.get_lat_long() == (14.7167, 17.467)
