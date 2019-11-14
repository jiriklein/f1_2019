from queue import Queue
from threading import Event, Thread

from f1_2019.pipeline.producers import F1Producer
from f1_2019.pipeline.receiver import F1Receiver


def main():
    packet_queue = Queue()
    thread_end_event = Event()
    receiver = F1Receiver(output_q=packet_queue, thread_end_event=thread_end_event)
    producer = F1Producer(input_q=packet_queue, thread_end_event=thread_end_event)

    with open("data/test_filepath.bin", "wb") as output_file:
        receiver_thread = Thread(target=receiver.listen)
        producer_thread = Thread(target=producer.write_to_file(output_file))

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


if __name__ == "__main__":
    main()
