from lab_converter.lab2xyz.xyz import lab2xyz
import colormath

def test_xyz():
    xyz = lab2xyz(l=0, a=0, b=0)
    assert type(xyz) == colormath.color_objects.XYZColor