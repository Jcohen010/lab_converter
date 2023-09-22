from lab_converter.lab2xyz.rgb_value_checker import rgb_value_checker


def test_rgb_value_checker():
    rgb_dict = rgb_value_checker({'r' : 277, 'g' : 290, 'b' : 205})
    
    assert rgb_dict['r'] == 255 and rgb_dict['g'] == 255 and rgb_dict['b'] == 205

def test_rgb_value_checker_is_dict():
    rgb_dict = rgb_value_checker({'r' : 277, 'g' : 290, 'b' : 205})

    assert type(rgb_dict) == dict
