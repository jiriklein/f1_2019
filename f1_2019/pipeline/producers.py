from queue import Queue, Empty
from threading import Event
from typing import Dict, Union, AnyStr, IO, Any
import json


class F1Producer:
    _QUEUE_GET_TIMEOUT = 5.0

    def __init__(
        self, queue: Queue, end_event: Event, config: Dict[str, Union[str, int]] = None
    ):
        kafka_config = config or {"bootstrap.servers": "localhost:9092"}
        self._kafka_producer = None
        self._queue = queue
        self._end_event = end_event
        self.produced_messages = 0

    @classmethod
    def make_kafka_packet(cls, topic_name: str, payload: dict) -> Dict[str, Any]:
        return dict(topic=topic_name, key="telemetry", value=json.dumps(payload))

    def write_to_file(self, file_output: IO[AnyStr]) -> None:
        while True and not self._end_event.is_set():
            try:
                packet = self._queue.get(True, self._QUEUE_GET_TIMEOUT)
                file_output.write(packet)
                self.produced_messages += 1

            except Empty:
                if self._end_event.is_set():
                    print("End event detected. Closing producer thread.")
                    break
                else:
                    continue
