from lab_converter.hex import lab2hex

def test_hex_len():
    hex = lab2hex(l=55, a=42, b=-10, hex_conversion_csv_path="./Base10_Hex.csv")

    assert len(hex) == 7
