from app import create_app
from app.decode import decode

flask_app = create_app()

def test_decode_ABCD():
    decoded_message = decode("CDEF", 2)
    assert decoded_message == "ABCD"

def test_encode_TESTE():
    decoded_message = decode("VGUVG", 2)
    assert decoded_message == "TESTE"

def test_encode_XYZ():
    decoded_message = decode("ZAB", 2)
    assert decoded_message == "XYZ"

def test_encode_ABCD_negative():
    decoded_message = decode("ZAB", -2)
    assert decoded_message == "XYZ"
