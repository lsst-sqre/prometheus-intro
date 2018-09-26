from prometheus_client import start_http_server, Gauge
import random
import time

# Create a metric to track the time spent processing a request.
REQUEST_TIME = Gauge("request_processing_time",
                     "Time spent processing a request.")


@REQUEST_TIME.time()
def process_request(t):
    time.sleep(t)


if __name__ == '__main__':
    # Start up the server to expose the metrics
    start_http_server(8000)

    # Generate some requests
    while True:
        process_request(random.random())
