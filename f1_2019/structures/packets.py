from ctypes import LittleEndianStructure

from f1_2019.structures.structures import (
    PACKET_HEADER,
    PACKET_MOTION_DATA,
    PACKET_SESSION_DATA,
    PACKET_LAP_DATA,
    PACKET_TELEMETRY_DATA
)


class PacketHeader(LittleEndianStructure):
    # pack constant indicates tight packing (i.e. no byte-padding)
    # this is inherited all the way from _StructUnionMeta
    _pack_ = 1
    # fields is the ctypes schema in structures file
    _fields_ = PACKET_HEADER

    @staticmethod
    def read_from(buf: bytes) -> LittleEndianStructure:
        header = PacketHeader.from_buffer_copy(buf)
        packet_type = header["packet_id"]
        packet_class = PACKET_TYPES.get(packet_type, PacketHeader)
        return packet_class(packet_type, buf)


class PacketMotionData(PacketHeader):
    _fields_ = PACKET_MOTION_DATA


class PacketSessionData(PacketHeader):
    _fields_ = PACKET_SESSION_DATA


class PacketLapData(PacketHeader):
    _fields_ = PACKET_LAP_DATA


class PacketEventData(PacketHeader):
    pass


class PacketParticipantsData(PacketHeader):
    pass


class PacketCarSetupData(PacketHeader):
    pass


class PacketCarTelemetryData(PacketHeader):
    _fields_ = PACKET_TELEMETRY_DATA


class PacketCarStatusData(PacketHeader):
    pass


PACKET_TYPES = {
    0: PacketMotionData,
    1: PacketSessionData,
    2: PacketLapData,
    3: PacketEventData,
    4: PacketParticipantsData,
    5: PacketCarSetupData,
    6: PacketCarTelemetryData,
    7: PacketCarStatusData,
}