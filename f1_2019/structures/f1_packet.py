PACKET_HEADER = {}
MOTION_DATA_STRUCTURE = {}


class F1Packet:
    HEADER = PACKET_HEADER

    def __init__(self, packet_type: int, buf: bytes):
        self._packet_type = packet_type
        if hasattr(self.__class__, "STRUCTURE"):
            self.data = self.STRUCTURE  # here we work with named tuples
        else:
            self.data = {}

    @staticmethod
    def read_from(buf: bytes):
        header = F1Packet.HEADER  # here we work with named tuples
        packet_type = header["packet_id"]  # & 0x3
        packet_class = PACKET_TYPES.get(packet_type, F1Packet)
        return packet_class(packet_type, buf)


class PacketMotionData(F1Packet):
    STRUCTURE = MOTION_DATA_STRUCTURE

    def __init__(self, packet_type: int, buf: bytes):
        super().__init__(packet_type, buf)
        self._data_remainder = buf


class PacketSessionData(F1Packet):
    pass


class PacketLapData(F1Packet):
    pass


class PacketEventData(F1Packet):
    pass


class PacketParticipantsData(F1Packet):
    pass


class PacketCarSetupData(F1Packet):
    pass


class PacketCarTelemetryData(F1Packet):
    pass


class PacketCarStatusData(F1Packet):
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