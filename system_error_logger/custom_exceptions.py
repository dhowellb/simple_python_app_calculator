import datetime

class BaseLogger:

    def __init__(self, log_file_name="error_logs.txt"):
        self.log_file_name = log_file_name
    def write_error(self, error_message):
        timestamp_string = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.log_file_name, "a") as log_file_object:
            log_file_object.write(f"[{timestamp_string}] RUNTIME ERROR: {error_message}\n")