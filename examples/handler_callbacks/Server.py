import sys

# add uplink directory to path
sys.path.insert(0, "../../")
import uplink
from uplink import *

BASE_URL="https://www.google.com"

def print_status(response):
    print(f'Google response status:{response.status_code}')
    return response

def handle_error(exc_type, exc_val, exc_tb):
    print(
        f'Error encountered. Exception will be raised. Exception Type:{exc_type}'
    )

@headers({"Accept": "text/html"})
class Google(Consumer):
    @response_handler(print_status)
    @get("/")
    def homepage(self):
        print('google home page')

    @error_handler(handle_error)
    @get("/bad_page.html")
    def bad_page(self):
        pass