import logging
import logging.handlers
import json
from mod7.task8.task8_server import app
class LogsCollectionHandler(logging.handlers.HTTPHandler):
    def __init__(self):
        super().__init__("127.0.0.1:5000", "/post_logs", method="POST")
        self.app = app

    def emit(self, record: logging.LogRecord):
        self.app.post(json.dumps(super().mapLogRecord(record)))


