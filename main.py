from lab_converter.hex import lab2hex
from lab_converter.rgb import lab2rgb
from lab_converter.lab2xyz.xyz import lab2xyz



if __name__ == "__main__":
    print(lab2hex(52.9, 8.88, 54.53, hex_conversion_csv_path="./Base10_Hex.csv"))
