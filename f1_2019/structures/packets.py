from ctypes import LittleEndianStructure

from f1_2019.structures.structures import PACKET_HEADER, PACKET_MOTION_DATA


class PacketHeader(LittleEndianStructure):
    # pack constant indicates tight packing (i.e. no byte-padding)
    # this is inherited all the way from _StructUnionMeta
    _pack_ = 1
    # fields is the ctypes schema
    _fields_ = PACKET_HEADER

    def __init__(self, fmt: str, packet_type: int, buf: bytes):
        super().__init__(fmt)
        self._packet_type = packet_type
        if hasattr(self.__class__, "STRUCTURE"):
            self.data = self.STRUCTURE  # here we work with named tuples
        else:
            self.data = {}

    @staticmethod
    def read_from(buf: bytes):
        header = PacketHeader.HEADER  # here we work with named tuples
        packet_type = header["packet_id"]  # & 0x3
        packet_class = PACKET_TYPES.get(packet_type, PacketHeader)
        return packet_class(packet_type, buf)


class PacketMotionData(PacketHeader):
    _fields_ = PACKET_MOTION_DATA

    def __init__(self, packet_type: int, buf: bytes):
        super().__init__(packet_type, buf)
        self._data_remainder = buf


class PacketSessionData(PacketHeader):
    pass


class PacketLapData(PacketHeader):
    pass


class PacketEventData(PacketHeader):
    pass


class PacketParticipantsData(PacketHeader):
    pass


class PacketCarSetupData(PacketHeader):
    pass


class PacketCarTelemetryData(PacketHeader):
    pass


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