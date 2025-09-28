import queue
import time
import random

request_queue = queue.Queue()

def generate_request():
    request_id = random.randint(1000, 9999)
    request_queue.put(request_id)
    print(f"Заявка {request_id} додана до черги.")

def process_request():
    if not request_queue.empty():
        request_id = request_queue.get()
        print(f"Заявка {request_id} оброблена.")
    else:
        print("Черга порожня.")

try:
    while True:
        if random.random() < 0.6:
            generate_request()
        process_request()
        time.sleep(1)
except KeyboardInterrupt:
    print("\nЗавершення роботи.")
