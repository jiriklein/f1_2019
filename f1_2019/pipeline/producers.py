from queue import Queue, Empty
from threading import Event
from typing import Dict, Union, AnyStr, IO, Any, List
import json

from f1_2019.models.participant import Participant
from f1_2019.structures.packets import CarTelemetryData


class F1Producer:
    _QUEUE_GET_TIMEOUT = 5.0

    def __init__(
        self,
        input_q: Queue,
        thread_end_event: Event,
        config: Dict[str, Union[str, int]] = None,
    ):
        kafka_config = config or {"bootstrap.servers": "localhost:9092"}
        self._kafka_producer = None
        self._queue = input_q
        self._end_event = thread_end_event
        self.produced_messages = 0

    @classmethod
    def make_kafka_packet(cls, topic_name: str, payload: dict) -> Dict[str, Any]:
        return dict(topic=topic_name, key="telemetry", value=json.dumps(payload))

    def resolve_packet_type(self, participants: List[Participant]):
        while True and not self._end_event.is_set():
            try:
                packet = self._queue.get(True, self._QUEUE_GET_TIMEOUT)
                if isinstance(packet, CarTelemetryData):
                    self._update_participants(packet, participants)

            except Empty:
                if self._end_event.is_set():
                    print("End event detected. Closing producer thread.")
                    break
                else:
                    continue

    @staticmethod
    def _update_participants(packet: CarTelemetryData, participants: List[Participant]) -> List[Participant]:
        player_car_idx = packet.header.player_car_index
        telemetry_data_player = packet.car_telemetry_data[player_car_idx]

        # player car always first for now
        participants[0].brake = telemetry_data_player.brake
        participants[0].speed = telemetry_data_player.speed
        participants[0].steer = telemetry_data_player.steer
        participants[0].engine_rpm = telemetry_data_player.engine_rpm

        return participants

    def write_to_file(self, file_output: IO[AnyStr]) -> None:
        while True and not self._end_event.is_set():
            try:
                packet = self._queue.get(True, self._QUEUE_GET_TIMEOUT)
                if hasattr(packet, "lap_data"):
                    print(packet.lap_data[0].total_distance)
                # file_output.write(packet)
                self.produced_messages += 1

            except Empty:
                if self._end_event.is_set():
                    print("End event detected. Closing producer thread.")
                    break
                else:
                    continue
