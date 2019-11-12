class F1Packet:
    HEADER = PACKET_HEADER

    def __init__(self, packet_type: int, buf: bytes):
        self._packet_type = packet_type
        if hasattr(self.__class__, "STRUCTURE"):
            self.data = self.STRUCTURE.read_dict(buf)
        else:
            self.data = {}


class PacketMotionData(F1Packet):
    pass


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