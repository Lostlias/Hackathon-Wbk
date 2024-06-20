import requests
from utils.utils import convert_bitarray_to_int
from bitarray import bitarray

def ampel_grün(ip, port, Token):
    # schaltet Ampel an der Fifo-Bahn aus
    url = "http://" + ip + "/iolink/v1/devices/master1port" + port + "/processdata/value"
    process_data = [
        convert_bitarray_to_int('00010001'),  # byte 0
        convert_bitarray_to_int('00000001'),  # byte 1
        convert_bitarray_to_int('00000000'),  # byte 2
        convert_bitarray_to_int('00000001'),  # byte 3

    ]
    header = {"Authorization": "Bearer " + Token}
    content = {"ioLink": {"valid": True, "value": process_data}}
    response = requests.post(url, json=content, headers=header)
    #print(response.content)

def ampel_orange(ip, port, Token):
    # schaltet Ampel an der Fifo-Bahn aus
    url = "http://" + ip + "/iolink/v1/devices/master1port" + port + "/processdata/value"
    process_data = [
        convert_bitarray_to_int('00110011'),  # byte 0
        convert_bitarray_to_int('00000011'),  # byte 1
        convert_bitarray_to_int('00000000'),  # byte 2
        convert_bitarray_to_int('00000001'),  # byte 3

    ]
    header = {"Authorization": "Bearer " + Token}
    content = {"ioLink": {"valid": True, "value": process_data}}
    response = requests.post(url, json=content, headers=header)
    #print(response.content)


def ampel_rot(ip, port, Token):
    # schaltet Ampel an der Fifo-Bahn aus
    url = "http://" + ip + "/iolink/v1/devices/master1port" + port + "/processdata/value"
    process_data = [
        convert_bitarray_to_int('00100010'),  # byte 0
        convert_bitarray_to_int('00000010'),  # byte 1
        convert_bitarray_to_int('00000000'),  # byte 2
        convert_bitarray_to_int('00000001'),  # byte 3

    ]
    header = {"Authorization": "Bearer " + Token}
    content = {"ioLink": {"valid": True, "value": process_data}}
    response = requests.post(url, json=content, headers=header)
    #print(response.content)

def ampel_blau(ip, port, Token):
    # schaltet Ampel an der Fifo-Bahn aus
    print("ok3")
    url = "http://" + ip + "/iolink/v1/devices/master1port" + port + "/processdata/value"
    process_data = [
        convert_bitarray_to_int('01000100'),  # byte 0
        convert_bitarray_to_int('00000100'),  # byte 1
        convert_bitarray_to_int('00000000'),  # byte 2
        convert_bitarray_to_int('00000001'),  # byte 3

    ]
    header = {"Authorization": "Bearer " + Token}
    content = {"ioLink": {"valid": True, "value": process_data}}
    response = requests.post(url, json=content, headers=header)
    #print(response.content)


def ampel_aus(ip, port, Token):
    # schaltet Ampel an der Fifo-Bahn aus
    url = "http://" + ip + "/iolink/v1/devices/master1port" + port + "/processdata/value"
    process_data = [
        convert_bitarray_to_int('00010001'),  # byte 0
        convert_bitarray_to_int('00000001'),  # byte 1
        convert_bitarray_to_int('00000000'),  # byte 2
        convert_bitarray_to_int('00000001'),  # byte 3

    ]
    header = {"Authorization": "Bearer " + Token}
    content = {"ioLink": {"valid": True, "value": process_data}}
    response = requests.post(url, json=content, headers=header)
    #print(response.content)
