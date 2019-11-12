import struct


def unpack_partial(fmt: str, data: bytes) -> tuple:
    size = struct.calcsize(fmt)
    return struct.unpack(fmt, data[:size]), data[size:]
