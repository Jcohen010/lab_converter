from lab_converter.rgb import lab2rgb

def test_rgb_round():
    rgb_dict = lab2rgb(l=55, a=42, b=-10)
    assert type(rgb_dict['r']) == int and type(rgb_dict['g']) == int and type(rgb_dict['b']) == int