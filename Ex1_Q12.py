class RequestResponseLogger:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(RequestResponseLogger, cls).__new__(cls)
            # Initialize logger properties here
            cls._instance.log_entries = []
        return cls._instance

    def log_request(self, request_details):
        # Log the request details
        log_entry = f"Request: {request_details}"
        self.log_entries.append(log_entry)

    def log_response(self, response_details):
        # Log the response details
        log_entry = f"Response: {response_details}"
        self.log_entries.append(log_entry)

    def get_logs(self):
        # Get all logged entries
        return self.log_entries


if __name__ == '__main__':

    logger1 = RequestResponseLogger()
    logger2 = RequestResponseLogger()
    # Both instances point to the same object
    print(logger1 is logger2)
    # Log requests and responses using the logger
    logger1.log_request("GET /api/data")
    logger2.log_response("200 OK")
    # Retrieve the logs from either instance
    logs = logger1.get_logs()
    print(logs)
