import json
import logging

class JsonFormatter(logging.Formatter):
    def format(self, record):
        log_record = {
            "levelname": record.levelname,
            "asctime": self.formatTime(record, self.datefmt),
            "module": record.module,
            "process": record.process,
            "thread": record.thread,
            "message": record.getMessage(),
        }
        
        if record.exc_info:
            log_record["exc_info"] = self.formatException(record.exc_info)
            
        return json.dumps(log_record, ensure_ascii=False)