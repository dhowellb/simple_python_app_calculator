import datetime

class BaseLogger:

    def __init__(self, log_file_name="error_logs.txt"):
        self.log_file_name = log_file_name