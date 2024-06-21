import json
import struct
import requests
from bitarray import bitarray


def bytearray_to_float32(bytearr):
    # hex_vals = [f'0x{byte:02x}' for byte in bytearr]
    arr = bytearray(bytearr)
    return struct.unpack('>f', arr)[0]


def bytearray_to_int16(bytearr):
    # hex_vals = [f'0x{byte:02x}' for byte in bytearr]
    arr = bytearray(bytearr)
    return struct.unpack('>h', arr)[0]


def convert_bitarray_to_int(bits: str) -> int:
    bits = bitarray(bits)
    return struct.unpack("<B", bits)[0]


def getJSONdata(obj, key):
    data = json.loads(obj)
    values = data[key]
    return values


def createJSON(data):
    json_data = json.dumps(data)
    return json_data

def convert_bitarray_to_int(bits: str) -> int:
    from bitarray import bitarray
    import struct
    bits = bitarray(bits)
    return struct.unpack("<B", bits)[0]

# noinspection HttpUrlsUsage
def get_token(ip):
    # gibt Bearer Token des angeschlossenen IO-Masters zurück
    ip = "172.22.192.101"
    url = "http://" + ip + "/api/balluff/v1/users/login"
    head = {"username": "admin", "password": "BNIEIP"}
    response = requests.post(url, json=head)
    print(response)
    output = str(response.content)
    output = output.split(":")
    output = output[1]
    output = output.replace("}", "")
    output = output.replace("'", "")
    output = output.replace('"', "")
    print(output)
    return output
