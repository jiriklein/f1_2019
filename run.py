from queue import Queue
from threading import Event, Thread
from typing import List
import time

import streamlit as st

from f1_2019.pipeline.producers import F1Producer
from f1_2019.pipeline.receiver import F1Receiver
from f1_2019.models.participant import Participant


def f1_pipeline(participants: List[Participant]):
    packet_queue = Queue()
    thread_end_event = Event()
    receiver = F1Receiver(output_q=packet_queue, thread_end_event=thread_end_event)
    producer = F1Producer(input_q=packet_queue, thread_end_event=thread_end_event)

    receiver_thread = Thread(target=receiver.listen)
    producer_thread = Thread(target=producer.resolve_packet_type, args=(participants,))

    # set threads to daemonic as we want them to be independent and die on sys exit
    thread_list = [receiver_thread, producer_thread]
    for _thread in thread_list:
        _thread.setDaemon(True)

    receiver.connect()
    for _thread in thread_list:
        _thread.start()

    # enter interaction loop as other threads are running in the background
    while True:
        try:
            choice = input("> ")
            # if the user writes end, stop all processing gracefully and exit
            if choice.lower() == "end":
                thread_end_event.set()
                for _thread in thread_list:
                    _thread.join()
                break

            if choice.lower() in [
                "messages",
                "count",
                "message count",
                "msg count",
                "msg",
            ]:
                print(
                    f"Received message count: {receiver.received_messages}\n"
                    + f"Produced message count: {producer.produced_messages}"
                )

        except KeyboardInterrupt:
            thread_end_event.set()
            receiver_thread.join()
            producer_thread.join()
            break


participant_list = [Participant() for i in range(20)]
game = Thread(target=f1_pipeline, args=(participant_list,))
game.daemon = True


if __name__ == "__main__":
    st.title("F1 Dashboard")
    game.start()

    empty_element = st.empty()
    while True:
        empty_element.text(dict(participant_list[0]))
        time.sleep(1)
