import logging

class ExcludeStaticFilter(logging.Filter):
    """
    Filter out access logs for static files (requests starting with /static/)
    """
    def filter(self, record):
        # The WSGI server logs the request. The message might be passed directly
        # or as arguments. Check the formatted message.
        message = record.getMessage()
        if 'GET /static/' in message or 'POST /static/' in message:
            return False
        return True
