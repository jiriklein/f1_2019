from queue import Queue
import socket
import struct
from threading import Event

from f1_2019.structures.packets import PacketHeader


class F1Receiver:
    _MULTICAST_ANY = "224.0.0.1"
    _SOCKET_TIMEOUT = 10.0

    def __init__(self, output_q: Queue, thread_end_event: Event, port: int = 20777):
        self._queue = output_q
        self._port = port
        self._end_event = thread_end_event
        self._socket = None
        self.received_messages = 0

    def connect(self) -> None:
        # internet + udp connection opts
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self._socket.settimeout(self._SOCKET_TIMEOUT)

        # Bind to the server address
        self._socket.bind(("", self._port))
        group = socket.inet_aton(self._MULTICAST_ANY)
        _req = struct.pack("4sL", group, socket.INADDR_ANY)
        self._socket.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, _req)

    def listen(self) -> None:
        while True and not self._end_event.is_set():
            try:
                data, address = self._socket.recvfrom(1400)
                packet = PacketHeader.unpack(data)
                if packet:
                    self._queue.put(packet)
                    self.received_messages += 1

            except socket.timeout:
                # check whether the event is set now
                if self._end_event.is_set():
                    print("End event detected. Closing receiver thread.")
                    break
                else:
                    continue
