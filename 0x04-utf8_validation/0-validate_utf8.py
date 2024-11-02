#!/usr/bin/python3

def validUTF8(data):
    bytes_remaining = 0
    mask1 = 1 << 7
    mask2 = 1 << 6

    for byte in data:
        byte = byte & 0xFF

        if bytes_remaining == 0:
            if (byte >> 5) == 0b110:
                bytes_remaining = 1
            elif (byte >> 4) == 0b1110:
                bytes_remaining = 2
            elif (byte >> 3) == 0b11110:
                bytes_remaining = 3
            elif (byte >> 7) == 0b0:
                bytes_remaining = 0
            else:
                return False
        else:
            if not (byte & mask1 and not (byte & mask2)):
                return False
            bytes_remaining -= 1

    return bytes_remaining == 0
