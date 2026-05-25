from pythonjsonlogger import jsonlogger
from config.middleware import client_ip_var

class CustomJsonFormatter(jsonlogger.JsonFormatter):
    def add_fields(self, log_record, record, message_dict):
        super().add_fields(log_record, record, message_dict)
        client_ip = client_ip_var.get()
        if client_ip:
            log_record['client_ip'] = client_ip
