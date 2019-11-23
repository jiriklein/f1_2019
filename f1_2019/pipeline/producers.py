from queue import Queue, Empty
from threading import Event
from typing import Dict, Union, AnyStr, IO, Any, List
import json

from f1_2019.models.participant import Participant


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

    def update_participants(self, participants: List[Participant]) -> None:
        while True and not self._end_event.is_set():
            try:
                packet = self._queue.get(True, self._QUEUE_GET_TIMEOUT)
                for participant in participants:
                    pass

            except Empty:
                if self._end_event.is_set():
                    print("End event detected. Closing producer thread.")
                    break
                else:
                    continue

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
