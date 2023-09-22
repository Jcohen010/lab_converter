from lab_converter.lab2xyz.read_conversion_csv import extract_store_base10_hex_conversion

def test_xyz():
    conversion_df = extract_store_base10_hex_conversion("./Base10_Hex.csv")
    assert conversion_df.columns.to_list() == ['base10', 'hex']